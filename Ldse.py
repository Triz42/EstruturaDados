#LDSE

class No():
    def __init__ (self, valor, proximo):
        self.info = valor
        self.prox = proximo
class Ldse():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
            
        self.quant+=1
    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
   
        self.quant+=1
    def removerInicio(self):
        if self.quant == 0:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
    def getUlt(self):
        return self.ult.info
    def getPrim(self):
        return self.prim.info
    def show(self):
        aux = self.prim
        i = 0
        while i < self.quant:
            print("aux: ", aux.info)
            aux = aux.prox
            i+=1
    def estaVazio():
        return self.quant == 0
    
    def removerFim(self):
        #tem que fazer
        aux = self.prim
        auxiliador = self.prim
        i = 0
        while i<self.quant:
            if self.quant == 1:
                self.prim = self.ult = None
            else:
                if auxiliador == self.ult:
                   self.ult = aux.prox = None
            i+=1
        self.quant-=1

