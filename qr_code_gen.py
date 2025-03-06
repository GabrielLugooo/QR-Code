# QRCode Generator

# Importar la librerías necesarias
import qrcode
import qrcode.constants


qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=7,
                    border=2)

qr.add_data('https://linktr.ee/gabriellugooo')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('gabriellugo_QR.png')

