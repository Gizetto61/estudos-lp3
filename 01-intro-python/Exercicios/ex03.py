# Faça um código que recebe o valor de uma compra e com base nele aplique desconto se possível
'''
    entre R$0,01 e R$9,99 desconte de 0%
    entre R$10,00 e R$99,99 desconto de 5%
    entre R$100,00 e R$499,99 desconto de 10%
    superior ou igual a R$500,00 desconto de 15%
'''

print('SISTEMA DE DESCONTOS!')

compra = input('O que você comprou? ')
valor = float(input('Qual é o valor da compra? '))

if valor >= 0.01 and valor <= 9.99:
    desconto = valor
    print('A compra ', compra,' não possui nenhum valor para desconto')
elif valor >= 10.00 and valor <= 99.99:
    desconto = valor * 0.05
    preço = valor - desconto
    print('A compra ', compra,' recebeu um desconto de 5%!')
    print('Seu valor passou a ser de R$', preço)
elif valor >= 100.00 and valor <= 499.99:
    desconto = valor * 0.10
    preço = valor - desconto
    print('A compra ', compra,' recebeu um desconto de 10%!')
    print('Seu valor passou a ser de R$', preço)
else:
    desconto = valor * 0.15
    preço = valor - desconto
    print('A compra ', compra,' recebeu um desconto de 15%!')
    print('Seu valor passou a ser de R$', preço)
