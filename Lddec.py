class No():
    def __init__(self, anterior, valor, proximo):
        self.anterior = anterior
        self.info = valor
        self.proximo = proximo

class Lddec():
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
            self.prim.proximo = self.prim.anterior = self.prim
        else:
            self.prim.anterior = self.ult.proximo = No(self.ult,valor,self.prim)
        self.quant+=1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
            self.prim.proximo = self.prim.anterior = self.prim
        else:
            self.ult.prox = self.ult = self.prim.ant = No(self.ult, valor, self.prim)
        self.quant +=1


    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
            self.quant -= 1
        else:
            self.prim = self.prim.prox
            self.prim.anterior = self.ult
            self.ult.proximo = self.prim
            self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
            self.quant -= 1
        else:
            self.ult = self.ult.ant
            self.ult.proximo = self.prim
            self.quant -=1

    def show(self):
        ct = 0
        aux = self.prim
        while ct < self.quant:
            print(aux.info)
            aux = aux.proximo
            ct += 1
            
    def showReverso(self):
        ct = 0
        aux = self.ult
        while ct < self.quant:
            print(aux.info)
            aux = aux.anterior
            ct += 1

    def inserirDepois(self, valor1, valor2):
        if(self.quant == 0):
            self.inserirInicio();
        elif(self.quant == 1):
            self.ult = self.prim.proximo = self.prim.anterior = No(self.prim, valor1, self.prim)
            self.quant += 1
        else:
            aux = self.prim
            ct = 0
            while ct < self.quant:
                if valor2 == aux.info and valor2 != self.ult.info:
                    aux.prox.anterior = aux.proximo = No(aux, valor1, aux.proximo)
                    self.quant += 1

                elif valor2 == aux.info and valor2 == self.ult.info:
                    aux.prox = self.ult = No(aux, valor1, self.prim)
                    self.quant += 1
                

                aux = aux.prox
                ct += 1
 
