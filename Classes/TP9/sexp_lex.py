#calc_sexp_lex.py
import ply.lex as lex

tokens = ['num','id',
            'ADD','SUB','MUL','DIV',
            'READ','PRINT','SET','DUMP']
literals = ['(',')']

t_ADD = r'add'
t_SUB = r'sub'
t_MUL = r'mul'
t_DIV = r'div'
t_READ = r'read'
t_PRINT = r'print'
t_SET = r'set'
t_DUMP = r'dump'
t_num = r'\d+'
t_id = r'[A-Z]'

def t_error(t):
    print("Caracter Ilegal: ", t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\n"

lexer = lex.lex()