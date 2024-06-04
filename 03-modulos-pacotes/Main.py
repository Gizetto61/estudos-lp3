#importa tudo do Modulo Matematica
#print(Matematica.PI)
import Matematica
from Matematica import *

#importa elemento por elemento (constantes, funções, atributos)
#from Matematica import PI
#from Matematica import somar
#from Matematica import subtrair
from Matematica import PI, somar, subtrair

#Conflito de nome
from Matematica import PI as Pi, somar as soma, subtrair as sub

print(PI)
print(somar(10.0, 3.2))
print(subtrair(10.0, 3.2))