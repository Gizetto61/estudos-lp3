'''Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).'''

print('Seja Bem Vindo ao seu...\n')
print('VERIFICADOR DE PALÍNDROMOS\n')

texto = input('\nDigite qualquer palavra ou frase e veja se é PALÍNDROMO! ')

def VerificaPalin(texto):
    TextoJunto = texto.replace(' ','')
    TextoMin = TextoJunto.lower()
    Palindromo = TextoMin[::-1]
    if Palindromo == TextoMin:
        print('\n\nO texto digitado é um Palíndromo!')
    else:
        print('\n\nO texto digitado não é um Palíndromo!')

VerificaPalin(texto)