'''Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário.'''

def ContaPalavras(string):
    string = string.lower()
    palavras = string.split()
    contador = []

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return contador

i = 1
while i == 1:

    print('Bem Vindo ao seu contador de Palavras!\n\n')
    i = int(input('Deseja continuar? [0] para não e [1] para sim: '))
    if i == 1:
        string = input('Digite uma Frase: ')
        resultado = ContaPalavras(string)
        print('Contagem de palavras:')
        for palavra, contador in resultado.items():
            print(f'{palavra}: {contador}')
    else:
        break