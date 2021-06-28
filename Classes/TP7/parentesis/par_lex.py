# par_lex.py
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

tokens = ['PA','PF']

import ply.lex as lex

t_PA = r'\('

t_PF = r'\)'

def t_error(t):
    print("Caracter Ilegal: ", t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()