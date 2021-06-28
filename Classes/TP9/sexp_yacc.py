import ply.yacc as yacc
import sys
from sexp_lex import tokens
from sexp_lex import literals

# Producao
def p_Comando_ler(p):
    "Comando : '(' READ id ')'"
    valor = input("Introduza um valor inteiro: ")
    p.parser.registers.update({p[3]: int(valor)})

def p_Comando_escrever(p):
    "Comando : '(' PRINT Exp ')'"
    print(p[3])

def p_Comando_atrib(p):
    "Comando : '(' SET id Exp ')'"
    p.parser.registers.update({p[3]: p[4]})

def p_Comando_despejar(p):
    "Comando : DUMP"
    print(p.parser.registers)

def p_Exp_add(p):
    "Exp : '(' ADD Exp Termo ')'"
    p[0] = p[3] + p[4]

def p_Exp_sub(p):
    "Exp : '(' SUB Exp Termo ')'"
    p[0] = p[3] - p[4]

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Exp : '(' MUL Termo Factor ')'"
    p[0] = p[3] * p[4]

def p_Termo_div(p):
    "Termo : '(' DIV Termo Factor ')'"
    if p[4] != 0:
        p[0] = p[3] / p[4]
    else:
        print("Erro: divisao por 0. A continuar com o dividendo ", p[3])
        p[0] = p[3]

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_Factor_num(p):
    "Factor : num"
    p[0] = int(p[1])

def p_Factor_id(p):
    "Factor : id"
    p[0] = p.parser.registers.get(p[1])

def p_error(p):
    print("Erro Sintatico ",p)
    
# Build Parser
parser = yacc.yacc()

# Creating the model
parser.registers = {}

# Read Input and Parse by line
import sys
for linha in sys.stdin:
    result = parser.parse(linha)
