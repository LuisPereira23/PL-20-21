#calc_sexp_lex.py
import ply.lex as lex

tokens = ['num','id']
literals = ['(',')','+','-','*','/','=','?','!']

t_num = r'\d+'

t_id = r'[a-z]'

def t_error(t):
    print("Caracter Ilegal: ", t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()