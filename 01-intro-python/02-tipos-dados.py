# Tipos de Dados
# int, float
# string, list, tuple, set
# dict
# None


# int
idade = 16
temperatura = 25

# float
altura = 1.73
PI = 3.14

# string
nome = 'Giovanni Zorzetto'
nome2 = "Giovanni Oliveira"


# Ecesso de caracter na string
print(nome[0])

# nome é um objeto da classe str
# e tem Métodos!!
# Para acessá-los basta digitar nome. 

print(nome.capitalize())


# Interpolação de strings
# f-string
nome3 = "João"
idade = 22
mensagem = f'Olá {nome3}, você tem {idade} anos!'

print(mensagem)


# list = lista de valores
# Pode ser alterado

# Lista vazia
habilidades = []
# Lista com valores diferentes
habilidades = ['java', 'python', 'sql', 'html', 10, True]
habilidades[0] = 'javac0'
print(habilidades[0])

habilidades.append


# Tupla
# 'lista' de valores que não podem ser alterados

habilidades = ('java', 'css', 'python')
opções = ('sim', 'não', 'talvez')


# set = não permite elementos duplicados na lista

emails = {'gigiozetto@gmail.com', 'zorzetto.oliveira@aluno.ifsp.edu.br', 'gigiozetto@gmail.com'}
print(emails)


# dict = dicionario
# chave : valor

# site de emprego
"""empresa = 'Google'
título = 'engenheiro de software'
salario = 20,000.00
remoto = True
"""
# vaga
vaga = {
    'empresa' : 'Google',
    'título' : 'engenheiro de software',
    'salario' : 20000.00,
    'remoto' : True
}

print(vaga['salario'])


# None = nulo
nome = None

def gerar_boletim(prontuário):
    # se encontrou no banco. retorna o boletim
    return 'boletim'
    # se não
    return None
