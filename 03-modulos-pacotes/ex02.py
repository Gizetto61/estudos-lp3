from ex02Calc import *

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em M: "))
print("=========================")

peso_ideal = CalcPesoIdeal(altura)

print("Você está: " + VerificaImc(peso, altura))
print(f"Precisa ganhar ou perder {peso_ideal} Kg para atingir IMC 24,9")