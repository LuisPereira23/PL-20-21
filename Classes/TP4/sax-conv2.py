import re

f = open('relatorio.xml')

#read first line

l = f.readline()

configs = re.search(r'<\?xml.+\?>', l)[0]

encoding = re.search(r'encoding="(.+)"', configs)[1]

print('<!DOCTYPE html>')

for line in f:

    if m := re.search(r'(?:(<\w+>))?([^<]*)(?:(</\w+>))?', line.strip()):

        for g in m.groups():

            print(g)

f.close()