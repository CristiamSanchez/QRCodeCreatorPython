#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar un código QR a partir de una URL
"""

import qrcode
import os
from datetime import datetime

# URL que se convertirá a código QR
url = "https://cristiamsanchez.github.io/CV-MonicaA/"

# Crear instancia de QR Code
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Tamaño de cada caja en píxeles
    border=4,  # Borde en cajas
)

# Agregar datos
qr.add_data(url)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill_color="black", back_color="white")

# Definir nombre del archivo con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
nombre_archivo = f"qr_code_{timestamp}.png"

# Guardar imagen
img.save(nombre_archivo)

print("Codigo QR generado exitosamente")
print(f"Archivo: {nombre_archivo}")
print(f"URL: {url}")
print(f"Directorio: {os.path.abspath('.')}")
