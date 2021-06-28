# Matriculas de outro mundo
# ex: 99-12-09-37
import re

latLong = re.compile(r'(^\([+\-]?([1-8]?[0-9](\.[0-9]+)?|90(\.0+)?), [+\-]?((([1-9]?[0-9]|1[0-7][0-9])(\.[0-9]+)?)|180(\.0+)?)\)$)')

f = open("latitudes.txt")


for linha in f:
    res = latLong.search(linha)
    if(res):
        print(res)
        print("VALIDO")
    else:
        print(linha)
        print("Invalido")
