def valida_entrada():
    '''checka se o numero está entre 1 e 15 e se é algarismo ou não'''
    while True :
        try :
            numero = int(input('Entre com um numero entre 1 e 15: '))
        except ValueError:
            print('Insira o númeor em algarismo!')
            continue

        if 1 <= numero <= 15 :
            return numero
        else :
            print('Número inválido.')

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