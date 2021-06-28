#aula5: 2021-03-23, jcr
#
#Somador on/off
#   -Semaforo esta on de inivio
#   -le do input
#   -reagir a estimulos
#   Ligar: r'[oO][nN]' ou r'(O|o)(n|N)'
#   Desligar: r'[Oo][Ff]{2}' ou r'(O|o)(f|F)(f|F)'
#   r'=' --> escrever valor acumulado
#   r'\d+' --> acrescentar o valor lido ao acumulado
#   qq outra coisa --> descartar

import sys
import re

# My state
soma = 0
semaforo = True

# Reading input
for linha in sys.stdin:
    if res := re.findall(r'([oO][nN])|([Oo][Ff]{2})|(=)|(\d+)',linha):
        for (on, off, pr, num) in res:
            if on:
                semaforo = True
            elif off:
                semaforo = False
            elif pr:
                print("soma = ",soma)
            elif num:
                if semaforo:
                    soma = soma + int(num)
    else:
        pass


