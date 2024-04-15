'''Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.'''

print('\nBem Vindo ao seu CONVERSOR DE NOTAS ESCOLARES!\n')
gpa = float(input('\nDigite a sua pontuação de 0 a 100: '))

def Converte(gpa):
    #Convertendo para a escala 10
    gpa10 = gpa / 10
    #Convertendo para a escala 4 Americana
    gpa4 = (gpa10 * 4) / 10
    
    #Verificando qual a Letra
    if gpa4 <= 4 and gpa4 > 3:
        print('Sua nota em Letras é A!')
    elif gpa4 <= 3 and gpa4 > 2:
        print('Sua nota em Letras é B!')
    elif gpa4 <= 2 and gpa4 > 1:
        print('Sua nota em Letras é C!')
    elif gpa4 <= 2 and gpa4 > 1:
        print('Sua nota em Letras é D!')
    else:
        print('Sua nota em Letras é F!')

Converte(gpa)
