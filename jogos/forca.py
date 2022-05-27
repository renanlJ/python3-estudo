def jogar():
    print('*********************************')
    print('***Bem vindo no jogo de forca!***')
    print('*********************************')

    palavra_secreta = "pera".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        print(letras_acertadas)
        enforcou = 6 == erros
        acertou = "_" not in letras_acertadas

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()