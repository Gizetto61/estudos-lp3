def VerificaImc(peso, altura):
    IMC = peso / (altura * altura)
    print(f"IMC de: {IMC}")

    if (IMC < 18.5):
        print("Abaixo do Peso!")
    elif (IMC >= 18.5 and IMC < 24.9):
        print("Peso Normal!")
    elif (IMC >= 24.9 and IMC < 29.9):
        print("Excesso de Peso!")
    elif (IMC >= 29.9 and IMC < 34.9):
        print("Obesidade de Classe 1!")
    elif (IMC >= 34.9 and IMC < 39.9):
        print("Obesidade de Classe 2!")
    elif (IMC >= 40.0):
        print("Obesidade de Classe 3!")

def CalcPesoIdeal(altura):
    imc_ideal = 24.9
    imc_ideal = imc_ideal * (altura ** 2)