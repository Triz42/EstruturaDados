import Les

l = Les.Les()

l.inserirFim("A")
if not l.estaCheio():
    l.inserirFim("B")
l.inserirFim("C")
l.inserirFim("D")
l.inserirFim("E")
if not l.estaCheio():
    l.inserirFim("F")
l.show()
l.inserirInicio("J")
l.removerInicio()
l.show()
