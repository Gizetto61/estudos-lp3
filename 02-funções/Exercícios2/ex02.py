'''Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.'''

print('Bem vindo ao seu Programa de TABUADA!!!\n')
numero = int(input('Digite um número para saber a sua Tabuada: \n'))

def imprime_tabua(numero):
    print('\nTABUADA:')
    print(f'[{numero}] X [1] = [{numero * 1}]')
    print(f'[{numero}] X [2] = [{numero * 2}]')
    print(f'[{numero}] X [3] = [{numero * 3}]')
    print(f'[{numero}] X [4] = [{numero * 4}]')
    print(f'[{numero}] X [5] = [{numero * 5}]')
    print(f'[{numero}] X [6] = [{numero * 6}]')
    print(f'[{numero}] X [7] = [{numero * 7}]')
    print(f'[{numero}] X [8] = [{numero * 8}]')
    print(f'[{numero}] X [9] = [{numero * 9}]')
    print(f'[{numero}] X [10] = [{numero * 10}]')

imprime_tabua(numero)