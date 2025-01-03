# Scraping photo profile Facebook

UK:

### Вимоги ###
- Python 3.8+
- Google Chrome (оновлений)
- ChromeDriver, який сумісний з вашою версією Chrome
- Встановлені залежності з `requirements.txt`

### Встановлення ###

1. Клонуйте репозиторій:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Створіть віртуальне оточення:
    ```bash
    python -m venv .venv
    source .venv/bin/activate      # Для Linux/MacOS
    .venv\Scripts\activate         # Для Windows
    ```

3. Встановіть залежності:
    ```bash
    pip install -r requirements.txt
    ```

4. Створіть конфігураційний файл:
    Створіть файл `config.json` у кореневій папці, використовуючи шаблон:
    ```json
    {
        "driver_path": "шлях_до_chromedriver",
        "phone": "ваш_номер_телефону",
        "password": "ваш_пароль"
    }
    ```

### Запуск ###

1. Активуйте віртуальне оточення, якщо воно ще не активне:
    ```bash
    source .venv/bin/activate      # Для Linux/MacOS
    .venv\Scripts\activate         # Для Windows
    ```

2. Запустіть скрипт:
    ```bash
    python main.py
    ```

### Рекомендації ###

- **Оновлення ChromeDriver**: Переконайтесь, що використовуєте відповідну версію ChromeDriver для вашого браузера Chrome.


---

## English Version ###

### Requirements
- Python 3.8+
- Google Chrome (updated)
- ChromeDriver compatible with your Chrome version
- Installed dependencies from `requirements.txt`

### Installation ###

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate      # For Linux/MacOS
    .venv\Scripts\activate         # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a configuration file:
    Create a `config.json` file in the root folder using the template:
    ```json
    {
        "driver_path": "path_to_chromedriver",
        "phone": "your_phone",
        "password": "your_password"
    }
    ```

### Running ###

1. Activate the virtual environment, if it's not activated:
    ```bash
    source .venv/bin/activate      # For Linux/MacOS
    .venv\Scripts\activate         # For Windows
    ```

2. Run the script:
    ```bash
    python main.py
    ```

### Recommendations ###

- **Update ChromeDriver**: Make sure you are using the correct version of ChromeDriver for your version of Chrome.

