import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generar_contrasena(numletsig, caracteres, solo_numeros=False):
    if solo_numeros:
        return ''.join(str(random.randint(0, 9)) for _ in range(caracteres))
    return ''.join(random.choice(numletsig) for _ in range(caracteres))

def generar_y_mostrar_contrasena():
    opcion = opcion_var.get()
    caracteres = int(caracteres_entry.get())

    if opcion == 1:
        solo_numeros = True
        numletsig = string.digits
    elif opcion == 2:
        solo_numeros = False
        numletsig = string.ascii_letters + string.digits
    else:
        solo_numeros = False
        numletsig = string.ascii_letters + string.digits + string.punctuation

    contrasena = generar_contrasena(numletsig, caracteres, solo_numeros)
    pyperclip.copy(contrasena)  # Copiar la contraseña al portapapeles
    messagebox.showinfo("Contraseña generada", f"La contraseña es: {contrasena}\n\n¡La contraseña ha sido copiada al portapapeles!")

# Crear ventana principal
root = tk.Tk()
root.title("Generador de contraseñas")

# Variables
opcion_var = tk.IntVar(value=1)

# Widgets
opcion_label = tk.Label(root, text="¿Cómo quieres la contraseña?")
opcion_label.pack()

opciones_frame = tk.Frame(root)
opciones_frame.pack()

opcion1_radio = tk.Radiobutton(opciones_frame, text="Solo números", variable=opcion_var, value=1)
opcion1_radio.pack(anchor='w')

opcion2_radio = tk.Radiobutton(opciones_frame, text="Números y letras", variable=opcion_var, value=2)
opcion2_radio.pack(anchor='w')

opcion3_radio = tk.Radiobutton(opciones_frame, text="Números, letras y símbolos", variable=opcion_var, value=3)
opcion3_radio.pack(anchor='w')

caracteres_label = tk.Label(root, text="Elige la longitud de la contraseña (8, 10 o 20):")
caracteres_label.pack()

caracteres_entry = tk.Entry(root)
caracteres_entry.pack()

generar_button = tk.Button(root, text="Generar contraseña", command=generar_y_mostrar_contrasena)
generar_button.pack()

# Ejecutar la aplicación
root.mainloop()
