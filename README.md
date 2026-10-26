# QR Code Creator Python

Genera una imagen PNG con código QR para la URL configurada en `generar_qr.py`.

## Requisitos

- Python 3.8 o una versión posterior.
- `pip`, incluido normalmente con Python.

## Windows

1. Descarga el proyecto:

   ```powershell
   git clone https://github.com/CristiamSanchez/QRCodeCreatorPython.git
   cd QRCodeCreatorPython
   ```

   También puedes descargar el repositorio como archivo ZIP desde GitHub y abrir una terminal dentro de la carpeta extraída.

2. Crea un entorno virtual e instala las dependencias:

   ```powershell
   py -m venv .venv
   .\\.venv\\Scripts\\Activate.ps1
   python -m pip install -r requirements.txt
   ```

   Si PowerShell no permite activar el entorno, ejecuta una vez:

   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```

3. Ejecuta el programa:

   ```powershell
   python generar_qr.py
   ```

## Linux

1. Instala Python, `pip`, entornos virtuales y Git. En Ubuntu o Debian:

   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv git
   ```

2. Descarga el proyecto:

   ```bash
   git clone https://github.com/CristiamSanchez/QRCodeCreatorPython.git
   cd QRCodeCreatorPython
   ```

3. Crea un entorno virtual e instala las dependencias:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```bash
   python3 generar_qr.py
   ```

## Resultado

El programa genera un archivo con el formato `qr_code_AAAAMMDD_HHMMSS.png` en la carpeta actual. La URL utilizada es la que aparece en la variable `url` de `generar_qr.py`.
