#Criar um índice de autores, que mapeie cada autor nos respectivos registos identifcados pela
#respectiva chave de citação (a 1a palavra a seguir à chaveta, que é única em toda a BD)

import re



dicionarioFinal={}


f = open("Trabalho/exemplo-utf8.bib", encoding="utf8")
flag=True

def colocarNomes(lista , chave):
    
    for i in lista: 
        if i in dicionarioFinal:
           
            # Ver se o tipo do valor é do tipo lista
            if not isinstance(dicionarioFinal[i], list):
                # Se não, converter em lista
                dicionarioFinal[i] = [dicionarioFinal[i]]
            # Append do valor à lista
            dicionarioFinal[i].append(chave)
        else:
            
            #Adicionar valor e chave
            if(i!=""):
               
                dicionarioFinal[i] = chave
    
            


for line in f:
    
    if(flag):
        if chave := re.search(r'@\w+{((?i:.+)),', line):
            chavez=chave.group(1)

        elif autoresCompleto := re.search(r'author *= *("|{)(.+)("|})', line):
            lista=autoresCompleto.group(2).split(" and ")
            lista = [x.strip(' ') for x in lista]
            colocarNomes(lista,chavez)
    
        elif autoresIncompleto := re.search(r'author *= *("|{)(.+)\n',line):
            zat=''
            zat=autoresIncompleto.group(2)
            flag=False

    else:
        if resto := re.search(r' *(.+)("|})+',line):
            zat=zat + " " +resto.group(1)
            lista=zat.split(" and" )
            lista = [x.strip(' ') for x in lista]
            colocarNomes(lista,chavez)
            zat=''
            flag=True
        else:
            resto = re.search(r' *(.+)',line)
            zat=zat + " " + resto.group(1)
            

t = open("Trabalho/out.txt", "w", encoding="utf-8")

for i in dicionarioFinal:
    t.write(str(i) + "->" + str(dicionarioFinal[i]) + "\n")
    



