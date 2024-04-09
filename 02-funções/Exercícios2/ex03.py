'''Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.'''

print('Bem Vindo! Esse programa\nconta o número de vogais e consoantes\npresentes na sua palavra!')

def conta_vogais(palavra):
    contador = []
    for letra in palavra:
        if letra in 'aeiou':
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    return contador

def conta_consoantes(palavra):
    contador1 = []
    for letra1 in palavra1:
        if letra1 in 'bcdfghjklmnpqrstvwxyz':
            if letra1 in contador1:
                contador1[letra1] += 1
            else:
                contador1[letra1] = 1
    return contador1

palavra = input('Digite uma PALAVRA: ')

vogais = conta_vogais(palavra)
for l in vogais:
    print(f'A quantidade de {l} foi {vogais[l]}')

consoantes = conta_consoantes(palavra)
for k in consoantes:
    print(f'a quantidade de {k} foi {consoantes[k]}')