import tkinter as tk
from entrada import Entrada

class PantallaBienvenida:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenida a Buscaminas")

        self.centrar_ventana(500, 500)  # Centrar la ventana de tamaño 400x300

        # Marco para centrar el contenido
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Logo y nombre del juego
        self.logo_label = tk.Label(self.frame, text="🧨", font=("Helvetica", 100))  # Simulando un logo con emoji
        self.logo_label.pack(pady=20)

        self.nombre_label = tk.Label(self.frame, text="Juego Buscaminas", font=("Helvetica", 32))
        self.nombre_label.pack(pady=10)

        # Botón para continuar
        self.boton_continuar = tk.Button(self.frame, text="Continuar", command=self.mostrar_configuracion)
        self.boton_continuar.pack(pady=20)

    def centrar_ventana(self, ancho, alto):
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        self.root.geometry(f'{ancho}x{alto}+{x}+{y}')

    def mostrar_configuracion(self):
        self.root.destroy()
        root_config = tk.Tk()
        app = Entrada(root_config)
        root_config.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaBienvenida(root)
    root.mainloop()
