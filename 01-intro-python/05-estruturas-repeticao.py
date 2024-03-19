# for

palavra = 'Python'
for letra in palavra:
    print(letra)

numeros = {1, 2, 3, 4, 5}
for numero in numeros:
    print(numero)

# range
# range(5) = 0. 1, 2, 3, 4

# range(start, stop)
# range(4, 10) = 4, 5, 6, 7, 8, 9, 10

# range(start, stop, step)
# range(3, 10, 2) = 4, 5, 7, 9

for i in range(10):
    print(i)


# while

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break
# para/pula o loop

numeros = {1, 2, 3, 4, 5} # parar o loop no primeiro número par
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break

# continue
# pula a interação

for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

# Compreenção de lista

numeros = [2, 3, 4]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

quadrados = [numero ** 2 for numero in numeros]


numeros = [1, 3, 4, 5, 2, 6]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0]


palavras = ['olá', 'mundo', 'teste']
palavra2 = [palavra.upper() for palavra in palavras]