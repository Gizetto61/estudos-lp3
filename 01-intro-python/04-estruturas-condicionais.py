# if. else
# if condição:
#   codigo
# else:
#   codigo

idade = 20
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')

# if/elif/else
# criança = 0 a 12 anos
# adolescente = 12 a 17 anos
# adulto = 18 a 59 anos
# idoso = +60 anos

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')


# Condiçôes aninhadas
email = 'admin@email.com'
senha = '123'
'''
if email == 'admin@email.com':
    if senha == '123':
        print('Liberado')
    else:
        print('Erro')
else:
    print('Erro')
'''

if email == 'adimin@email.com' and senha == '123':
    print('Liberado')
else:
    print('Erro')

    


# Operador Ternário
idade = 17
# maior ou menor
status = ''

status = 'maior' if idade >= 18 else 'menor'

# match
dia = 3
match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case _:
        print('Dia Inválido')

match dia:
    case 1 | 7:
        print('Fim de Semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia Útil')
    case _:
        print('Dia Inválido')