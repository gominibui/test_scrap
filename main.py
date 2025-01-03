import os
import time
import logging
import uuid
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FacebookScraper:
    def __init__(self, driver_path: str, phone: str, password: str):
        self.driver_path = driver_path
        self.phone = phone
        self.password = password
        self.driver: Optional[webdriver.Chrome] = None

        # Logging settings
        logging.basicConfig(
            filename="out.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def create_driver(self) -> webdriver.Chrome:
        s = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=s)
        return self.driver

    def open_facebook(self) -> None:
        try:
            self.driver.maximize_window()
            self.driver.get("https://www.facebook.com/")
            logging.info("Opened Facebook site.")
        except Exception as e:
            logging.error("Error opening Facebook site: %s", e)
            raise

    def login_to_facebook(self) -> None:
        try:
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_input.send_keys(self.phone)
            logging.info("Phone number/email entered.")

            pass_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "pass"))
            )
            pass_input.send_keys(self.password)
            logging.info("Password entered")

            pass_input.send_keys(Keys.ENTER)
            logging.info("Enter was pressed.")
        except Exception as e:
            logging.error("Error logging in: %s", e)
            raise

    def go_to_profile(self) -> None:
        try:
            self.driver.get("https://www.facebook.com/me")
            logging.info("Opened profile page.")
            WebDriverWait(self.driver, 500)
        except Exception as e:
            logging.error("Error navigating to profile: %s", e)
            raise

    def get_profile_image_url(self) -> Optional[str]:
        try:
            image_url = self.driver.execute_script("""
                var image = document.querySelector("image");
                return image ? image.getAttribute("xlink:href") : null;
            """)
            return image_url
        except Exception as e:
            logging.error("Error finding image URL: %s", e)
            raise

    def save_image(self, image_url: str) -> None:
        try:
            folder_path = "d_image"
            os.makedirs(folder_path, exist_ok=True)

            response = requests.get(image_url)

            if response.status_code == 200:
                unique_filename = f"{int(time.time())}_{uuid.uuid4().hex}.jpg"
                file_path = os.path.join(folder_path, unique_filename)
                with open(file_path, "wb") as file:
                    file.write(response.content)
                logging.info(f"Image saved as {file_path}")
            else:
                logging.warning("Failed to download image. Status code: %d", response.status_code)

        except Exception as e:
            logging.error("Error saving image: %s", e)
            raise

    def scrape(self) -> None:
        try:
            self.create_driver()
            self.open_facebook()
            self.login_to_facebook()
            self.go_to_profile()

            image_url = self.get_profile_image_url()

            if image_url:
                self.save_image(image_url)
                logging.info("Image found. URL: %s", image_url)
                print("Image URL:", image_url)
            else:
                logging.warning("Image not found.")
                print("Image not found.")
        except Exception as e:
            logging.error("Error in the process: %s", e)
            print("Error:", e)
        finally:
            if self.driver:
                self.driver.quit()
                logging.info("Driver closed.")


def load_config(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error open json file: {e}")
        raise


if __name__ == "__main__":
    # load JSON file
    config = load_config("config.json")

    scraper = FacebookScraper(
        driver_path=config["driver_path"],
        phone=config["phone"],
        password=config["password"]
    )
    scraper.scrape()
