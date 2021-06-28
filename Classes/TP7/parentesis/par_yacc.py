# par_yacc.py
# Aula 7 jcr
# Linguagem dos parentises
# ()
# (())
# ()()(())
# ()((()))(((())))
#
# T = { '(' , ')' }
#
# p1: Par -> '(' Par ')' Par
# p2: Par -> vazio

# Reconhecimento de: ()()(())
# Par =p1=> '(' Par ')' Par =p2=> '(' ')' Par =p1=> '(' ')' '(' Par ')' Par
# =p2=> '(' ')' '(' ')' Par =p1=> '(' ')' '(' ')' '(' Par ')' Par
# =p1=> '(' ')' '(' ')' '(' '(' Par ')' Par ')' Par 
# =p2=p2=p2=> '(' ')' '(' ')' '(' '(' ')' ')'

import ply.yacc as yacc
from par_lex import tokens

def p_Par(p):
    "Par : PA Par PF Par"
    p.parser.pares += 1

def p_Par_empty(p):
    "Par : "
    pass

def p_error(p):
    print("Erro Sintatico ",p)
    parser.success = False
    
# Build Parser
parser = yacc.yacc()

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    parser.success = True
    parser.pares = 0

    parser.parse(linha)

    if parser.success:
        print("Frase Valida Reconhecida.")
        print("Numero de Pares: ", parser.pares)
    else:
        print("Frase Invalida. Corrija e tente de novo...")