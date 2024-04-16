'''Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.'''

import random

marcas = ['ford', 'chevrolet', 'fiat', 'peugeot', 'volkswagen', 'citroen', 'honda', 'toyota', 'renaut']

def exibirMarcas(escolhida, letrascertas):
    resultado = []
    for letra in escolhida:
        if letra in letrascertas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def Main():
    escolhida = random.choice(marcas)
    letrascertas = []
    chances = 6

    print('\n\nBem Vindo ao seu JOGO DA FORCA!')
    print('Tente acertar a palavra em menos de 6 tentativas\n\n\n')

    while chances > 0:
        print(f'Palavra: {exibirMarcas(escolhida, letrascertas)}')
        print(f'Tentativas Restantes: {chances}\n')
        letra = input('Digite uma letra: ').lower()

        if letra in escolhida:
            letrascertas.append(letra)
            if set(letrascertas) == set(escolhida):
                print('Parabéns! Marca Completa!')
                break
        else:
            print('Letra Incorreta. Tente De Novo')
            chances -= 1
    if chances == 0:
        print(f'Game Over! A Marca era {escolhida}')

Main()