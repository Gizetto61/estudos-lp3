# Função



# Somar uma lista de números
# Usar função sum
sum([1, 3, 5])

# Declaração
# def nome_função(parâmetro1, parâmetro2):
#   return(valor)
# Calcular média de números

def Calcula_média (n1, n2):
    med = (n1 + n2)/2
    print(f'A média é {med}')

Calcula_média(n1, n2)

# Chamada
# nome_função('dad', 1)
print('Olá')
sum([1, 3, 5])

# Função sem retorno e sem parâmetros

def imprimir_mensagem():
    print('Socorro')

imprimir_mensagem()
imprimir_mensagem()

# Função sem retorno com parâmetros

def saudações(nome):
    print(f'Bom dia {nome}')

saudações('Maria')
saudações('José')

# Função com retorno e sem parâmetros

def obter_mensagem():
    return "Socorro"

mensagem = obter_mensagem()
print(mensagem)

print(obter_mensagem())

# Função com retorno com parâmetros
# Mais adequada!!!
# Função Pura
def gerar_saudação(nome):
    return f'Bom dia {nome}'

print(gerar_saudação('Pedro'))
print(gerar_saudação('João'))

def saudação (nome, frase):
    print(f'{frase} {nome}')

saudação('João', 'Bom dia')

def saudação (nome, frase):
    return f'{frase} {nome}'

print(saudação('João', 'Bom dia'))


# Entrada
notas_alunos = [
    [9.0, 7.0, 3.0],
    [9.0, 4.0, 5.0],
    [8.0, 9.0, 4.0],
]

# Saída [6.3, 6.0, 7.0]

def calcular_média(valores):
    return sum (valores / len(valores))

def calcular_media_alunos(notas_alunos):
    ''' medias = []
    for notas in notas_alunos:
        media = calcular_média(notas)
        medias.append(media)

    return medias'''
    return [calcular_média(notas) for notas in notas_alunos]