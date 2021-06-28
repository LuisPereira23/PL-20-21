# abin_lex.py
#
# ()
# c
# (40 (20 () ()) (50 () ()))
#
# T = {'(',num,')'}
# p1: ABin -> '(' num ABin ABin ')'
# p2: ABin -> '(' ')'

import ply.yacc as yacc
import sys
from abin_lex import tokens

def p_ABin(p):
    "ABin : '(' num ABin ABin ')'"
    p[0] = "{\n\t\"root\": " + p[2] + ",\n\t\"left\": " + p[3] + ",\n\t\"right\": " + p[4] + "\n}"

def p_ABin_empty(p):
    "ABin : '(' ')' "
    p[0] = "null"

def p_error(p):
    print("Erro Sintatico ",p)
    
# Build Parser
parser = yacc.yacc()

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    result = parser.parse(linha)
    print(result)
