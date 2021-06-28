import re

latLong = re.compile(r'(^\([+\-]?([1-8]?[0-9](\.[0-9]+)?|90(\.0+)?), [+\-]?((([1-9]?[0-9]|1[0-7][0-9])(\.[0-9]+)?)|180(\.0+)?)\)$)')

n = int(input())

for i in range(n):
    linha = input()
    res = latLong.search(linha)
    if(res):
        print(res)
        print("VALIDO")
    else:
        print(linha)
        print("Invalido")
