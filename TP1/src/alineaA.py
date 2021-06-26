# Calcular o número de entradas por categoria; apresente a listagem em formato HTML por ordem
# alfabética

import re

f = open("Trabalho/exemplo-utf8.bib", encoding="utf8")
print('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n</head>\n<body>\n<h1> Numero de entradas por categoria </h1>')


categorias = {}
for line in f:
    m = re.search(r'^@(.+){', line)
    if m:
        m1 = m.group(1).lower()
        if m1 in categorias:
            categorias[m1] += 1
        else:
            categorias[m1] = 1


categorias = dict(sorted(categorias.items(), key=lambda p: p[0]))

print('<ol>')
for cat in categorias:
    print(f'<li> {cat} aparece {categorias[cat]} vezes </li>')
print('</ol>\n</body>\n</html>')


f.close()
