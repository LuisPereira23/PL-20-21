# p1: ArvBin -> '(' Cont ')'
# p2: Cont -> num ArvBin ArvBin
# p3:     | 
#
# Recursivo descendente para arvores binarias

from abin_lex import tokens
from abin_lex import lexer

def getSimb():
    tok = lexer.token()
    if tok:
        return tok.type

def erro(esperado,reconhecido):
    global listaErros
    listaErros.append(f'Estava a espera de {esperado} e recebi {reconhecido}')
    #print('Estava a espera de ',esperado,' e recebi ',reconhecido)

def rec_term(sim):
    global prox_simb
    if prox_simb == sim:
        prox_simb = getSimb()

def rec_ArvBin():
    global prox_simb
    if prox_simb == 'AP' :
        rec_term('AP')
        rec_Cont()
        rec_term('FP')
    else:
        erro('AP', prox_simb)

def rec_Cont():
    global prox_simb
    if prox_simb == 'NUM' :
        rec_term('NUM')
        rec_ArvBin()
        rec_ArvBin()
    elif prox_simb == 'FP':
        pass
    else:
        erro('NUM ou FP', prox_simb)

import sys

for linha in sys.stdin:
    listaErros = []
    lexer.input(linha)
    prox_simb = getSimb()
    rec_ArvBin()
    if len(listaErros) == 0:
        print('Frase reconhecida: ', linha)
    else:
        print('Erros sintaticos: ',len(listaErros))
        print(listaErros)

