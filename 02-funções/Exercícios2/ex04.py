''' Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor. '''

print('Bem Vindo ao seu programa SIMULADOR DE ELEIÇÕES!!\n\n')
def MostraPainel():
    print('========================')
    print('| CANDIDATOS!          |')
    print('========================')
    print('| Tiririca        | 10 |')
    print('| Pablo Marçal    | 17 |')
    print('| Palmito Gentili | 28 |')
    print('========================')

def Votos():
    i = 0
    j = 0
    while i == 0:
        MostraPainel()
        escolha = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        escolha[j] = int(input('\n\nDigite a sua escolha: '))
        j = j + 1
        continuar = int(input('\n\nDeseja votar em mais alguém? [1] para sim e [0] para não: '))
        if continuar == 1:
            i = 0
        else:
            i = 1

def CalculaVotos(escolha, j):
    Votos()
    quant10 = escolha.count(10)
    quant17 = escolha.count(17)
    quant28 = escolha.count(28)
    print(f'\n\nVocê votou {quant10} vezes no Tiririca, {quant17} vezes no Pablo Marçal e {quant28} vezes no Gentili\n\n')
    if quant10 < quant17 and quant10 < quant28:
        print('Tiririca foi o menos votado!\n')
    elif quant10 > quant17 and quant10 > quant28:
        print('Tiririca foi o mais votado!\n')
    else:
        print('Tiririca tá no meio!\n')
    
    if quant17 < quant10 and quant17 < quant28:
        print('Marçal foi o menos votado!\n')
    elif quant17 > quant10 and quant17 > quant28:
        print('Marçal foi o mais votado!\n')
    else:
        print('Marçal tá no meio!\n')
    
    if quant28 < quant17 and quant28 < quant10:
        print('Gentili foi o menos votado!\n')
    elif quant28 > quant17 and quant28 > quant10:
        print('Gentili foi o mais votado!\n')
    else:
        print('Gentili tá no meio!\n')

CalculaVotos(escolha = any, j = any)
