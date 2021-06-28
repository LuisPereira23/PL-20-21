import ply.yacc as yacc 
from capicua_lex import tokens
from capicua_lex import literals

def p_Capicua_zeros(p):
    "Capicua : ZERO ContZ "
    p[0] = "0" + p[2]

def p_Capicua_uns(p):
    "Capicua : UM ContU "
    p[0] = "1" + p[2]

def p_Capicua_vazia(p):
    "Capicua : "
    p[0] = ""

def p_ContZ_zero(p):
    "ContZ : Capicua ZERO"
    p[0] = p[1] + "0"

def p_ContZ_vazia(p):
    "ContZ : "
    p[0] = ""

def p_ContU_um(p):
    "ContU : Capicua UM"
    p[0] = p[1] + "1"

def p_ContU_vazia(p):
    "ContU : "
    p[0] = ""

def p_error(p):
    print("Erro Sintatico ",p)
    
# Build Parser
parser = yacc.yacc()

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    result = parser.parse(linha)
    print("Frase valida: ",result)
