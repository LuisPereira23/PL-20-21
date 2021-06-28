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

import ply.lex as lex
import sys 

# Token declarations
tokens = (
    'ON','OFF',
    'PRINT','NUM'
)

# Token with action
def t_NUM(t):
    r'\d+'
    if t.lexer.semaforo:
        t.lexer.soma = t.lexer.soma + int(t.value)

def t_ON(t):
    r'[oO][nN]'
    t.lexer.semaforo = True

def t_OFF(t):
    r'[Oo][Ff]{2}'
    t.lexer.semaforo = False

def t_PRINT(t):
    r'='
    print("Soma = ",t.lexer.soma)

# Traking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Characters ignored
t_ignore = " \t"

# Errors
def t_error(t):
    # print(f"Wrong Character {t.value[0]}")
    t.lexer.skip(1)


# build the lexer
lexer = lex.lex()

# My state
lexer.soma = 0
lexer.semaforo = True

# Reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass