from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import gspread
import pandas as pd
import Sender
import time

inicio = time.time()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
KEY = "key.json"
# Autenticación
credentials = Credentials.from_service_account_file(KEY, scopes=SCOPES)

# Acceso a Google Sheets
gc = gspread.authorize(credentials)

# Abre la hoja de cálculo por su nombre
spreadsheet = gc.open("Registro Future Makers 2025 (Respuestas)")

worksheet = spreadsheet.worksheet("Respuestas de formulario 1")

rows = worksheet.get_all_values()

df = pd.DataFrame(rows[1:], columns=rows[0])
print(df)

infos = []

for i in range(len(df)):
    nombre = df["Nombre"].tolist()[i]
    numero = df["Numero de teléfono"].tolist()[i]
    mensaje = f"hola {nombre} este es un mensaje de prueba"
    
    infos.append([numero, mensaje, nombre])

print(infos)

Sender.send(infos)
print("Todos los mensajes han sido enviados.")

fin = time.time()

print(f"Tiempo de ejecución: {fin-inicio} segundos.")
