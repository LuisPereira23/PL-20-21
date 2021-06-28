#aula5.1: 2021-03-23, jcr
# calclex.py
# Tokenizer para maquina calcular
#
#   in: (3-1)*5+8/3
#   out: PA NUM SUB NUM PF MUL NUM ADD NUM DIV NUM

import ply.lex as lex
import sys 

# Token declarations
tokens = (
    'PA','PF',
    'ADD','SUB',
    'MUL','DIV',
    'NUM'
)

# Token Regex
t_PA = r'\('
t_PF = r'\)'
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'

# Token with action
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Traking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Characters ignored
t_ignore = " \t"

# Errors
def t_error(t):
    print(f"Wrong Character {t.value[0]}")
    t.lexer.skip(1)


# build the lexer
lexer = lex.lex()

# Reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)