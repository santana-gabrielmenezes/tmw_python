def valida_entrada():
    while True :
        try :
            numero = int(input('Entre com um numero entre 1 e 15: '))
            return numero
        except ValueError:
            print('Insira o númeor em algarismo!')

numero_sorte = 7

for i in range(3) :

    numero = valida_entrada()

    if numero == numero_sorte :
        print('Você acertou!')
        break
    elif numero > numero_sorte :
        print('Você errou! Tente um número menor')
    else :
        print('Você errou! Tente um número maior')