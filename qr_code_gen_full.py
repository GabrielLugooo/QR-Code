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