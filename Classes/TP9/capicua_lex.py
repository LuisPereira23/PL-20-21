import ply.lex as lex

tokens = ['ZERO','UM']
literals = ['.']

t_ZERO = r'0'

t_UM = r'1'

def t_error(t):
    print("Caracter Ilegal: ", t.value[0])
    t.lexer.skip(1)

t_ignore = " \t\n"

# Build lexer
lexer = lex.lex()