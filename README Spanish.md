<img align="center" src="https://i.imgur.com/ZgHWFhw.png" alt="gabriellugo" />

# GENERADOR DE CÓDIGO QR

<a href="https://github.com/GabrielLugooo/QR-Code/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Código%20QR%20Español-000000" alt="Código QR Español" /></a>
<a href="https://github.com/GabrielLugooo/QR-Code" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Código%20QR%20Inglés-green" alt="Código QR Inglés" /></a>

### Objetivos

Este proyecto permite generar un código QR a partir de una URL ingresada por el usuario a través de una interfaz gráfica creada con Tkinter. Se utiliza la biblioteca `qrcode` de Python para crear la imagen y guardarla en el sistema local.

El propósito de este proyecto es aprender a generar códigos QR de manera interactiva, personalizar su tamaño, corrección de errores y apariencia, así como manipular imágenes y construir interfaces gráficas en Python.

### Habilidades Aprendidas

- Uso de la biblioteca `qrcode` en Python.
- Generación de códigos QR programáticamente.
- Personalización de códigos QR (tamaño, corrección de errores, colores).
- Manipulación y almacenamiento de imágenes en Python.
- Creación de interfaces gráficas con `Tkinter`.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/TKinter-000000?logo=tkinter&logoSize=auto)
![Static Badge](https://img.shields.io/badge/QR%20Code-000000?logo=qrcode&logoSize=auto)

- Python.
- Librería `qrcode`.
- `Tkinter` (desarrollo de GUI) para la interfaz gráfica.
- Editor de código (VS Code).
- Sistema de archivos para almacenamiento de imágenes.

### Proyecto

#### Vista Previa

- Minimal Version

<img align="center" src="https://i.imgur.com/ndyntln.jpeg" alt="QRCode Minimal" />
<img align="center" src="https://i.imgur.com/NMmyect.png" alt="QRCode_01" width="150" height="150" />

- Full Version

<img align="center" src="https://i.imgur.com/MeLvMDE.jpeg" alt="QRCode Full" />
<img align="center" src="https://i.imgur.com/NMmyect.png" alt="QRCode_02_Full" width="150" height="150" />

#### Código con Comentarios (Español)

```python
# QRCode Generator Full

# Importar las librerias necesarias
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Definir la función generadora del QR
def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if img_path:
        img.save(img_path)
        messagebox.showinfo("Éxito", f"Código QR guardado en: {img_path}")

        img = Image.open(img_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de QR")
root.geometry("400x500")

# Etiqueta y campo de entrada
label = tk.Label(root, text="Ingrese la URL:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Botón para generar el QR
generate_btn = tk.Button(root, text="Generar QR", command=generate_qr)
generate_btn.pack(pady=20)

# Etiqueta para mostrar el QR generado
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
```

### Limitaciones

El Generador de Código QR es solo para fines educativos bajo la licencia MIT.
También esta disponible el código de la versión mínimal.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
