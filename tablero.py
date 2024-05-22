import random
from celda import Celda

class Tablero:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.celdas = [[Celda() for _ in range(columnas)] for _ in range(filas)]
        self.colocar_minas()
        self.calcular_numeros()

    def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if not self.celdas[fila][columna].es_mina:
                self.celdas[fila][columna].es_mina = True
                minas_colocadas += 1

    def calcular_numeros(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not self.celdas[fila][columna].es_mina:
                    self.celdas[fila][columna].numero = self.contar_minas_alrededor(fila, columna)

    def contar_minas_alrededor(self, fila, columna):
        contador = 0
        for i in range(max(0, fila-1), min(self.filas, fila+2)):
            for j in range(max(0, columna-1), min(self.columnas, columna+2)):
                if self.celdas[i][j].es_mina:
                    contador += 1
        return contador

    def revelar_celda(self, fila, columna):
        if not self.celdas[fila][columna].revelada and not self.celdas[fila][columna].marcada:
            self.celdas[fila][columna].revelar()
            if self.celdas[fila][columna].es_mina:
                return True
            if self.celdas[fila][columna].numero == 0:
                self.revelar_alrededor(fila, columna)
        return False

    def revelar_alrededor(self, fila, columna):
        for i in range(max(0, fila-1), min(self.filas, fila+2)):
            for j in range(max(0, columna-1), min(self.columnas, columna+2)):
                if not self.celdas[i][j].revelada:
                    self.revelar_celda(i, j)

    def marcar_celda(self, fila, columna):
        self.celdas[fila][columna].marcar()
