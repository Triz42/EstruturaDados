
print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')


palavra_secreta = "banana"

acertou = False
errou = False


while not acertou and not errou:
    print("Keep Going")
    chute = input('Qual letra? ')
    posicao = 0
    for letra in palavra_secreta:
        if chute.lower() == letra.lower():
            print("Encontei a letra {} na posção {}".format(letra, posicao))
        posicao = posicao + 1
