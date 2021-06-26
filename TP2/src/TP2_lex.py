# Analex para o recursivo descendente de arvores binarias

import ply.lex as lex

tokens = ['NUM','FNAM','INT','VAR','RUN','READ','WRITE','IF','ELSE','FOR','BOOL','BOOLEAN','OR','AND','MOD','EQUALS','INF','SUP','INFEQ','SUPEQ','RETURN', "TEXTO"]
literals = ['+','-','/','*','(',')','{','}','=',';','[',']']

def t_RETURN(p):
    r'return'
    return p

def t_SUPEQ(p):
    r'>='
    return p

def t_INFEQ(p):
    r'<='
    return p

def t_SUP(p):
    r'>'
    return p

def t_INF(p):
    r'<'
    return p

def t_EQUALS(p):
    r'=='
    return p

def t_MOD(p):
    r'mod'
    return p

def t_AND(p):
    r'and'
    return p

def t_OR(p):
    r'or'
    return p

def t_BOOLEAN(p):
    r'Boolean'
    return p

def t_BOOL(p):
    r'(False|True)'
    return p

def t_TRUE(p):
    r'True'
    return p

def t_FOR(p):
    r'for'
    return p

def t_IF(p):
    r'if'
    return p

def t_ELSE(p):
    r'else'
    return(p)

def t_READ(p):
    r'read'
    return p

def t_WRITE(p):
    r'write'
    return(p)

def t_RUN(p):
    r'run'
    return p

def t_NUM(p):
    r'\d+'
    return p

def t_INT(p):
    r'Int'
    return p

def t_VAR(p):
     r'[a-z]+\d*'
     return p

def t_FNAM(p):
    r'[A-Z]\w*'
    return p

def t_TEXTO(p):
    r'"[A-Za-z ]*"'
    return p

t_ignore= " \t\n"

def t_error(p):
    # print("Caracter ilegal: ",t.value[0])
    p.lexer.skip(1)
    return p

lexer = lex.lex()