# Enviar mensajes con Google Forms

Un script en Python que permite enviar múltiples mensajes personalizados a cada persona en una hoja de Google generada por un formulario de Google.

## Requisitos

- Python 3.7 o superior
- Google API Client Library para Python
- Selenium
- gspread
- pandas

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

3. Configura tu entorno:
    - Crea un proyecto en Google Cloud y habilita las APIs de Google Sheets y Google Drive.
    - Descarga el archivo de credenciales JSON y renómbralo a [key.json](http://_vscodecontentref_/1). Colócalo en el directorio raíz del proyecto.

## Uso

1. Inicializa el perfil de WhatsApp Web (solo la primera vez):
    ```sh
    python SoloEjecutarUnaVez.py
    ```

2. Ejecuta el script principal para enviar los mensajes:
    ```sh
    python main.py
    ```

## Estructura del Proyecto

- [main.py](http://_vscodecontentref_/2): Script principal que lee los datos de la hoja de Google y envía los mensajes.
- [Sender.py](http://_vscodecontentref_/3): Contiene la lógica para enviar mensajes a través de WhatsApp Web.
- [SoloEjecutarUnaVez.py](http://_vscodecontentref_/4): Inicializa el perfil de WhatsApp Web.
- [key.json](http://_vscodecontentref_/5): Archivo de credenciales para acceder a la API de Google.
- [README.md](http://_vscodecontentref_/6): Este archivo.
- [LICENSE](http://_vscodecontentref_/7): Licencia del proyecto.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](http://_vscodecontentref_/8) para más detalles.
