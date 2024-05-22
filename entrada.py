import tkinter as tk
from tkinter import messagebox
from game_buscaminas import JuegoBuscaminas

class Entrada:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuración de Buscaminas")

        self.label_filas = tk.Label(root, text="Número de filas:")
        self.label_filas.pack()
        self.entry_filas = tk.Entry(root)
        self.entry_filas.pack()

        self.label_columnas = tk.Label(root, text="Número de columnas:")
        self.label_columnas.pack()
        self.entry_columnas = tk.Entry(root)
        self.entry_columnas.pack()

        self.label_minas = tk.Label(root, text="Número de minas:")
        self.label_minas.pack()
        self.entry_minas = tk.Entry(root)
        self.entry_minas.pack()

        self.boton_inicio = tk.Button(root, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_inicio.pack()
        
    def __init__(self, root):
        self.root = root
        self.root.title("Configuración de Buscaminas")

        self.centrar_ventana(300, 150)  # Centrar la ventana de tamaño xxx x xxx

        self.label_filas = tk.Label(root, text="Número de filas:")
        self.label_filas.pack()
        self.entry_filas = tk.Entry(root)
        self.entry_filas.pack()

        self.label_columnas = tk.Label(root, text="Número de columnas:")
        self.label_columnas.pack()
        self.entry_columnas = tk.Entry(root)
        self.entry_columnas.pack()

        self.label_minas = tk.Label(root, text="Número de minas:")
        self.label_minas.pack()
        self.entry_minas = tk.Entry(root)
        self.entry_minas.pack()

        self.boton_inicio = tk.Button(root, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_inicio.pack()

    def centrar_ventana(self, ancho, alto):
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        self.root.geometry(f'{ancho}x{alto}+{x}+{y}')

    def iniciar_juego(self):
        try:
            filas = int(self.entry_filas.get())
            columnas = int(self.entry_columnas.get())
            minas = int(self.entry_minas.get())
            if filas > 0 and columnas > 0 and 0 < minas < filas * columnas:
                self.root.destroy()
                juego = JuegoBuscaminas(filas, columnas, minas)
                juego.jugar()
            else:
                messagebox.showerror("Error", "Número de minas debe ser positivo y menor al número de celdas del tablero.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


    def iniciar_juego(self):
        try:
            filas = int(self.entry_filas.get())
            columnas = int(self.entry_columnas.get())
            minas = int(self.entry_minas.get())
            if filas > 0 and columnas > 0 and 0 < minas < filas * columnas:
                self.root.destroy()
                juego = JuegoBuscaminas(filas, columnas, minas)
                juego.jugar()
            else:
                messagebox.showerror("Error", "Número de minas debe ser positivo y menor al número de celdas del tablero.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Entrada(root)
    root.mainloop()
