def Volume ():
    comp = float(input("Digite o Comprimento do Aquário: "))
    alt = float(input("Digite a Altura do Aquário: "))
    larg = float(input("Digite a Largura do Aquário: "))
    print("==============================")
    vol = (comp * alt * larg) / 1000
    return vol

def Termostato (vol):
    amb = float(input("Digite a Temperatura Ambiente: "))
    desej = float(input("Digite a Temperatura Desejada: "))
    print("==============================")
    pot = vol * 0,05 * (amb - desej)
    return pot