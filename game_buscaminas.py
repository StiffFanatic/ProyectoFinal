import pygame
import tkinter as tk
from tkinter import messagebox
from tablero import Tablero

class JuegoBuscaminas:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = Tablero(filas, columnas, minas)
        self.celda_tam = 30
        self.screen = pygame.display.set_mode((columnas * self.celda_tam, filas * self.celda_tam))
        self.juego_terminado = False
        self.ganado = False
        pygame.display.set_caption("Buscaminas")
        pygame.font.init()
        self.fuente = pygame.font.SysFont('Arial', 24)

    def jugar(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and not self.juego_terminado:
                    x, y = event.pos
                    fila = y // self.celda_tam
                    columna = x // self.celda_tam
                    if event.button == 1:  # Click izquierdo
                        self.tablero.revelar_celda(fila, columna)
                        if self.tablero.celdas[fila][columna].es_mina:
                            self.juego_terminado = True
                            self.ganado = False
                    elif event.button == 3:  # Click derecho
                        self.tablero.marcar_celda(fila, columna)
                self.verificar_ganador()
            self.mostrar_tablero()
            pygame.display.flip()
            clock.tick(30)
            if self.juego_terminado:
                self.mostrar_mensaje_fin_juego()
                return

    def mostrar_tablero(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                celda = self.tablero.celdas[fila][columna]
                rect = pygame.Rect(columna * self.celda_tam, fila * self.celda_tam, self.celda_tam, self.celda_tam)
                if celda.revelada:
                    if celda.es_mina:
                        pygame.draw.rect(self.screen, (255, 0, 0), rect)
                    else:
                        pygame.draw.rect(self.screen, (200, 200, 200), rect)
                        if celda.numero > 0:
                            text = self.fuente.render(str(celda.numero), True, (0, 0, 0))
                            self.screen.blit(text, (columna * self.celda_tam + 10, fila * self.celda_tam + 5))
                else:
                    pygame.draw.rect(self.screen, (150, 150, 150), rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
                if celda.marcada:
                    pygame.draw.line(self.screen, (0, 0, 0), (columna * self.celda_tam + 5, fila * self.celda_tam + 5), (columna * self.celda_tam + 25, fila * self.celda_tam + 25), 2)
                    pygame.draw.line(self.screen, (0, 0, 0), (columna * self.celda_tam + 25, fila * self.celda_tam + 5), (columna * self.celda_tam + 5, fila * self.celda_tam + 25), 2)

    def verificar_ganador(self):
        reveladas = 0
        for fila in self.tablero.celdas:
            for celda in fila:
                if celda.revelada and not celda.es_mina:
                    reveladas += 1
        if reveladas == self.filas * self.columnas - self.minas:
            self.juego_terminado = True
            self.ganado = True

    def mostrar_mensaje_fin_juego(self):
        mensaje = "¡Ganaste!" if self.ganado else "Perdiste"
        respuesta = messagebox.askyesno("Fin del Juego", f"{mensaje}\n¿Deseas jugar otra vez?")
        if respuesta:
            self.reiniciar_juego()
        else:
            pygame.quit()

    def reiniciar_juego(self):
        self.tablero = Tablero(self.filas, self.columnas, self.minas)
        self.juego_terminado = False
        self.ganado = False
        self.jugar()
