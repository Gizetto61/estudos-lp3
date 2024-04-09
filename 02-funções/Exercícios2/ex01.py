'''Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.'''
# Classe que seleciona valores automaticamente
import random

print('Bem Vindo! O computador escolherá um número de 1 a 100, tente acertar!\n')

# Método de seleciona um número inteiro aleatório de 1 a 100
comp = random.randint(1, 100)

i = True

while i == True:
    usuário = int(input('Digite um número e veja se está certo: '))
    
    def verifica_prox(usuário, comp):
        if usuário < comp:
            print('MAIS!')
            print('Tente Novamente\n')
        elif usuário > comp:
            print('MENOS!')
            print('Tente Novamente\n')
        elif usuário == comp:
            print('VOCÊ ACERTOU!!!\n')
            i = False
    
    verifica_prox(usuário, comp)