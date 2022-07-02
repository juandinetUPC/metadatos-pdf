"""
seleccionar un archivo usando tkinter y devolver la ruta
para usar fitz:
instalar python -m pip install --upgrade pymupdf
"""
import fitz
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

archivo = filedialog.askopenfilename(initialdir="Downloads", title="Seleccionar archivo", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
documento = fitz.open(archivo)
numero_paginas = documento.page_count
metadatos = documento.metadata
print("Páginas : ", numero_paginas)
print("Metadatos:")
for item in metadatos:
    print(item, ":", metadatos[item])

root.destroy()