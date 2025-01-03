FROM python:3.9-slim
LABEL author="Denis Naumenko"

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get -y --fix-broken install


RUN LATEST_CHROMEDRIVER=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/${LATEST_CHROMEDRIVER}/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /scraping_facebook
WORKDIR /scraping_facebook

CMD ["python", "main.py"]
