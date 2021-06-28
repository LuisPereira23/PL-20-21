# listas-yacc.py
# Aula 7 jcr
# Listas heterogeneas: inteiros e alfanumericos
# []
# [78]
# [1, 2, 3]
# [a, barco]
# [121, asa, c45]
#
# T = {number,'[',']',alfanum,','}
#
# Axioma - S
#
# p1: Lista -> '[' Elementos ']'
# p1.5 Lista -> '[' ']'
# p2: Elementos -> Elemento
# p3: Elementos -> Elementos ',' Elemento
# p4, p5: Elemento -> alfanum | number

import ply.yacc as yacc
from listas_lex import tokens

# Somente reconhecimento
def p_grammar(p):
    #String multilinha
    """
    Lista : PA Elementos PF

    Elementos : Elemento
              | Elementos VIRG Elemento

    Elemento : alfanum
             | number
    """

def p_error(p):
    print("Erro Sintatico ",p)
    parser.success = False

# Build Parser
parser = yacc.yacc()

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)

    if parser.success:
        print("Frase Valida Reconhecida.")
    else:
        print("Frase Invalida. Corrija e tente de novo...")