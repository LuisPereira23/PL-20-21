# Analex para o recursivo descendente de arvores binarias

import ply.lex as lex

tokens = ['NUM','AP','FP']

t_NUM = r'\d+'
t_AP =r'\('
t_FP=r'\)'

t_ignore= " \t\n"

def t_error(t):
    # print("Caracter ilegal: ",t.value[0])
    t.lexer.skip(1)
    return t

lexer = lex.lex()

# Tokenizer

#import sys 
#for linha in sys.stdin:
#    lexer.input(linha)
#    for tok in lexer:
#        print(tok)