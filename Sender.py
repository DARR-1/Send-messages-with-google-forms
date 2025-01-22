from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

CHROME_DATA_DIR = r"CHROME_DATA_DIR"
PROFILE_NAME = "PROFILE_NAME"


def send(infos):
    options = Options()
    options.add_argument(f"user-data-dir={CHROME_DATA_DIR}")
    options.add_argument(f"profile-directory={PROFILE_NAME}")

    # Configuración del controlador
    driver = webdriver.Chrome(
        options=options
    )  # Cambia a tu controlador correspondiente
    driver.get("https://web.whatsapp.com/")

    i = 1
    for info in infos:
        while True:
            try:
                start = time.time()
                # Busca al contacto o grupo por nombre
                contact_name = str(info[0])
                search_box = driver.find_element(
                    By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'
                )
                search_box.send_keys(contact_name)
                search_box.send_keys(Keys.RETURN)
            except Exception as e:
                if "no such element" in str(e):
                    continue

            try:
                # Envía el mensaje
                message_box = driver.find_element(
                    By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'
                )
            except Exception as e:
                if "no such element" in str(e):
                    continue

            message_box.send_keys(info[1])
            message_box.send_keys(Keys.RETURN)

            break
        print(
            f"Mensaje enviado a {info[2]} ({info[0]}) ||",
            f" {(i)/len(infos)*100}% completado.",
        )
        i += 1

        end = time.time()
        print(f"tiempo por mensaje: {end-start}")

    time.sleep(1)
    driver.quit()
