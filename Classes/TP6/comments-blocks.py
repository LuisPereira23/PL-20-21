# comments.py
# Aula6
#
import ply.lex as lex
import sys 

# Context Conditions
states = (
    ('comment','exclusive'),
    ('block','inclusive')
)

# Tokens
tokens = ['CBEGIN','CEND','CONTENT','BBEGIN','BEND','STRING']

# Rules for initial state
def t_STRING(t):
    r'\"[^"]*\"'
    print(t.value,end='')

def t_CBEGIN(t):
    r'/\*'
    t.lexer.push_state('comment')

def t_BBEGIN(t):
    r'\{'
    print('Entrei num bloco...')
    t.lexer.push_state('block')


def t_CONTENT(t):
    r'.|\n'
    print(t.value,end='')

# Rules for comment state
def t_comment_CEND(t):
    r'\*/'
    t.lexer.pop_state()

def t_comment_CONTENT(t):
    r'.|\n'
    t.lexer.skip(1)

# Rules for block state

def t_block_BEND(t):
    r'\}'
    print('Sai de um bloco...')
    t.lexer.pop_state()

# Error Rules
def t_ANY_error(t):
    print(f"Wrong Character {t.value[0]}")
    t.lexer.skip(1)


# build the lexer
lexer = lex.lex()

# Reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass