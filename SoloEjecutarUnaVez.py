from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

CHROME_DATA_DIR = r"C:\Users\diego\AppData\Local\Google\Chrome\User Data"
PROFILE_NAME = "Profile 1"


def initialize():
    options = Options()
    options.add_argument(f"user-data-dir={CHROME_DATA_DIR}")
    options.add_argument(f"profile-directory={PROFILE_NAME}")

    # Configuración del controlador
    driver = webdriver.Chrome(
        options=options
    )  # Cambia a tu controlador correspondiente
    driver.get("https://web.whatsapp.com/")

    # Escanea el código QR manualmente (solo necesario la primera vez)
    print("Escanea el código QR para iniciar sesión en WhatsApp Web.")
    time.sleep(30)  # Tiempo para escanear el QR
    driver.quit()


if __name__ == "__main__":
    initialize()
