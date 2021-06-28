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

def p_Lista(p):
    "Lista : PA Elementos PF"
    pass

def p_Lista_empty(p):
    "Lista : PA PF"

def p_Elementos(p):
    "Elementos : Elementos VIRG Elemento"
    p.parser.elems += 1

def p_Elementos_Elemento(p):
    "Elementos : Elemento"
    p.parser.elems += 1

def p_Elemento_number(p):
    "Elemento : number"
    p.parser.numbers.append(p[1])

def p_Elemento_alfanum(p):
    "Elemento : alfanum"
    p.parser.alfanum.append(p[1])

def p_error(p):
    print("Erro Sintatico ",p)
    parser.success = False

# Build Parser
parser = yacc.yacc()

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    parser.success = True
    parser.numbers = []
    parser.alfanum = []
    parser.elems = 0

    parser.parse(linha)

    if parser.success:
        print("Frase Valida Reconhecida.")
        print("Numero de elementos: ", parser.elems)
        print("Numeros: ", parser.numbers)
        print("Alfanum: ", parser.alfanum)
    else:
        print("Frase Invalida. Corrija e tente de novo...")