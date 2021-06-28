# Detecao de enderecos de email
import re
lista = []
email = re.compile(r'((\w+\.)*\w+@(\w+\.)*\w+)')
email2 = re.compile(r'(([a-zA-Z0-9_]+\.)*[a-zA-Z0-9_]+@([a-zA-Z0-9_]+\.)*[a-zA-Z0-9_]+)')

word = "[a-zA-Z0-9_]"
email3 = re.compile(rf'(({word}+\.)*{word}+@({word}+\.)*{word}+)')

n=int(input())
for i in range(n):
    linha = input()
    r1 = email.findall(linha)
    r2 = email2.findall(linha)
    r3 = email3.findall(linha)
    if(r1 or r2 or r3):
        for (e,_,_) in r1:
            lista.append(e)

lista.sort()
print(';'.join(lista))