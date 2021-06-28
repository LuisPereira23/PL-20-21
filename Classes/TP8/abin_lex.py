# abin_lex.py
#
# ()
# (15 () ())
# (40 (20 () ()) (50 () ()))
#
# T = {'(',num,')'}
# p1: ABin -> '(' num ABin ABin ')'
# p2: ABin -> '(' ')'

import ply.lex as lex

tokens = ['num']
literals = ['(',')']

t_num = r'[+\-]?\d+'

def t_error(t):
    print("Caracter Ilegal: ", t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()