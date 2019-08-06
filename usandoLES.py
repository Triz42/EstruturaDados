import Les

l = Les.Les()

l.inserirFim("A")
l.inserirFim("B")
if not l.estaCheio():
    l.inserirFim("C")

l.show()
l.removerFim()
l.show()

 
l.inserirFim("D")
l.inserirFim("E")
if not l.estaCheio():
    l.inserirFim("F")
l.show()
l.inserirInicio("J")
l.removerInicio()
l.show()
