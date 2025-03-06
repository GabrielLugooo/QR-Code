<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# QR CODE GENERATOR

<a href="https://github.com/GabrielLugooo/QR-Code" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20QR%20Code-000000" alt="English QR Code" /></a>
<a href="https://github.com/GabrielLugooo/QR-Code/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20QR%20Code-green" alt="Spanish QR Code" /></a>

### Objective

This project allows users to generate a QR code from a URL entered through a graphical interface created with Tkinter. The Python `qrcode` library is used to create and save the image locally.

The purpose of this project is to learn how to generate QR codes interactively, customize their size, error correction, and appearance, as well as handle images and build graphical interfaces in Python.

### Skills Learned

- Using the `qrcode` library in Python
- Programmatic QR code generation.
- QR code customization (size, error correction, colors).
- Image handling and saving in Python.
- Building graphical interfaces with `Tkinter`.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python.
- `qrcode` library.
- `Tkinter` (GUI development) for the graphical interface.
- Code editor (VS Code).
- File system for image storage.

### Project

#### Preview

- Minimal Version

<img align="center" src="https://i.imgur.com/ndyntln.jpeg" alt="QRCode Minimal" />
<img align="center" src="https://i.imgur.com/NMmyect.png" alt="QRCode_01" width="150" height="150" />

- Full Version

<img align="center" src="https://i.imgur.com/MeLvMDE.jpeg" alt="QRCode Full" />
<img align="center" src="https://i.imgur.com/NMmyect.png" alt="QRCode_02_Full" width="150" height="150" />

#### Code with Comments (English)

```python
# QRCode Generator Full

# Import the necessary libraries
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Define the QR generating function
def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
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
        messagebox.showinfo("Success", f"QR code saved in: {img_path}")

        img = Image.open(img_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

# Create the main window
root = tk.Tk()
root.title("QR Generator")
root.geometry("400x500")

# Label and input field
label = tk.Label(root, text="Enter the URL:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Button to generate the QR
generate_btn = tk.Button(root, text="Generate QR", command=generate_qr)
generate_btn.pack(pady=20)

# Label to display the generated QR
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Run the application
root.mainloop()
```

### Limitations

QR Code Generator it's just for educational purpose under the MIT License.
The code for the minimal version is also available.

---

<h3 align="left">Connect with me</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
