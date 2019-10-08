def mult(valor1, valor2):
    if valor1 == 0:
        print('v', valor1)
        return 0
    else:
        return valor2 + mult(valor1 - 1, valor2)
