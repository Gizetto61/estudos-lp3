# Operadores Aritméticos
# +, -, *, /, **
nota1 = 10
nota2 = 5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

#Número elevado a outro
#10 elevado a 2
numero = 10
potencia = numero * numero
# OU
potencia = numero ** 2


# Operadores Lógicos
# And, or, not
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

print(not True) #False
print(not False) #True


# permitir entrada
# - Quando o usuário for funcionário
# - Usuário não bloqueado
# - Hora atual entre 8h e 18h
# - Adm

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_adm = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

if usuario_adm or (funcionario_ativo and  horario_comercial):
    print('Acesso Permitido!')


# Operadores de Comparação
# ==, !=, >, <, >=, <=

nota1 = 10
nota2 = 5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3


if media >= 6.0:
    print('Aprovado!!')

# Operador de identidade
# is, is not
# comparar se os objetos ocupam o mesmo espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) #True
print(a is b) #False

c = b

print(c is b) #True


# Operador in
# verificar se um elemento existe ou não em uma sequencia
# Sting, list, tuple
opcoes = {'sim', 'não', 'talvez'}
opcao = input('Digite uma opção: ') #'                 SIM    '
opcao = opcao.lower().strip() #'sim'

if opcao in opcoes:
    print('ok')
else:
    print('não tem essa opção')

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numeros)