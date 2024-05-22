class Celda:
    def __init__(self, es_mina=False):
        self.es_mina = es_mina
        self.revelada = False
        self.marcada = False
        self.numero = 0

    def revelar(self):
        self.revelada = True

    def marcar(self):
        self.marcada = not self.marcada
