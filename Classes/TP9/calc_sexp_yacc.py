import ply.yacc as yacc
import sys
from calc_sexp_lex import tokens

# Producao
def p_Comando_ler(p):
    "Comando : '?' id"
    print ("(read",p[2], ")")

def p_Comando_escrever(p):
    "Comando : '!' Exp"
    print("print ", p[2], ")")

def p_Comando_atrib(p):
    "Comando : id '=' Exp"
    print("(set ", p[1]," ", p[3], ")")

def p_Comando_despejar(p):
    "Comando : '!' '!'"
    print("dump")

def p_Exp_add(p):
    "Exp : Exp '+' Termo"
    p[0] = "(add " + p[1] + " " + p[3] + ")"

def p_Exp_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = "(sub " + p[1] + " " + p[3] + ")"

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : Termo '*' Factor"
    p[0] = "(mul " + p[1] + " " + p[3] + ")"

def p_Termo_div(p):
    "Termo : Termo '/' Factor"
    if p[3] != "0":
        p[0] = "(div " + p[1] + " " + p[3] + ")"
    else:
        print("Erro: divisao por 0. A continuar com o dividendo ", p[1])
        p[0] = p[1]

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_Factor_num(p):
    "Factor : num"
    p[0] = p[1]

def p_Factor_id(p):
    "Factor : id"
    p[0] = p[1]

def p_error(p):
    print("Erro Sintatico ",p)
    
# Build Parser
parser = yacc.yacc()

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    result = parser.parse(linha)
