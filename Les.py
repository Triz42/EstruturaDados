class Les():
    
    def __init__(self):
        self.lista = [None, None, None, None, None]
        self.quant = 0
        
    def inserirFim(self,valor):
        self.lista[self.quant] = valor
        self.quant +=1

    def show(self):
        i = 0
        while i < self.quant:
            print(self.lista[i])
            i+=1
    def removerFim(self):
        self.quant -= 1

    def estaCheio(self): return self.quant == 5

    def estaVazio(self): return self.quant == 0

    def getPrim(self): return self.lista[0]

    def getUlt(self): return self.lista[self.quat -1]

    def inserirInicio(self, valor):
        self.lista[0] = valor

    def removerInicio(self):
        self.lista[0] = None
