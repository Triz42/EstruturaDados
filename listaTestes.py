lista = ['A','B','C',None, None]
quant = 3

#faça um código que insere 'X' na posição 0, empurrando os demais valores p/trás. Após a inserção incrementando quant
i=3
while i>0:
    lista[i]= lista[i-1]
    i-=1
quant+=1
lista[0] = 'X'
print(lista)
print("Quant: ", quant)


#faça um código que imprima do incio para o fim todos os valores da lista (None não deve ser considerado valor)
i=0
j = quant
while i<quant:
    print(lista[i])
    i+=1

#faça um código que insira 'y' na posição 0 empurrando os demais valores para trás. Apos a impressão incremente quant
i=quant
while i>0:
    lista[i]= lista[i-1]
    i-=1
quant+=1
lista[0] = 'Y'


#faça um código que remova o elemento da posção 0 e traga todos os demais para a frente. Apos, decremente o
#quant e imprima todos os valores nao nulos da lista do inicio para o fim
print('--------------')
i=0
quant = 4
while i<quant:
    lista[i]=lista[i+1]
    print(lista[i])
    i+=1
lista[quant] = None
print(lista)
