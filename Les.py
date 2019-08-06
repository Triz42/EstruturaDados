class Les():
    
    def __init__(self):
        self.vet = [None, None, None, None, None]
        self.quant = 0
        
    def inserirFim(self,valor):
        self.vet[self.quant] = valor
        self.quant +=1

    def show(self):
        i = 0
        while i < self.quant:
            print(self.vet[i])
            i+=1
    def removerFim(self):
        self.quant -= 1

    def estaCheio(self): return self.quant == 5

    def estaVazio(self): return self.quant == 0

    def getPrim(self): return self.vet[0]

    def getUlt(self): return self.vet[self.quat -1]

    def inserirInicio(self, valor):
        self.vet[0] = valor

    def removerInicio(self):
        self.vet[0] = None
