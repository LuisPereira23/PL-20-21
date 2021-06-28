# Matriculas de outro mundo
# ex: 99-12-09-37
import re

matricula = re.compile(r'(\b((\d\d\.{3}){3}|(\d\d-){3}|(\d\d:){3})\d\d\b)')

matriculas = []

f = open("matriculas.txt")

for linha in f:
    res = matricula.findall(linha)
    if(res):
        for (m,_,_,_,_) in res:
            matriculas.append(m)
            print(m)
    
print("Encontrei:",len(matriculas),"que sao:",matriculas)