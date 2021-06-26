#Construa um Grafo que mostre, para um dado autor (denido na altura pelo utilizador) todos os
#autores que publicam normalmente com o autor em causa.

import re
from graphviz import Digraph

def worker(docBib,author):

     # retirar linhas %
    docBib = re.sub(
        r'%(.)*',
        r'',
        docBib
    )

    # retirar linhas >
    docBib = re.sub(
        r'>.*\n+',
        r'',
        docBib
    )

    #retirar newlines
    docBib = re.sub(
        r'([À-ÿa-zA-Z,:\'\.\{\};=-])\n+',
        r'\1',
        docBib
    )

    #corrigir } @
    docBib = re.sub(
        r'} *@',
        r'\n}\n@',
        docBib
    )

    #corrigir } EOF
    docBib = re.sub(
        r'} *\Z',
        r'\n}\n',
        docBib
    )

    #corrigir #,
    docBib = re.sub(
        r' *= *([0-9]+)',
        r' = "\1"',
        docBib
    )

    #acrescentar newlines especificos
    docBib = re.sub(
        r'\",',
        r'",\n',
        docBib
    )

    #fix {""}
    docBib = re.sub(
        r'({.*)"(.*)"(.*})',
        r'\1\2\3',
        docBib
    )


    docBib = re.sub(
        r'(?i)},( *(author|title|note|booktitle|year|institution|type|keyword|editor|url|month|abstract|pages|number|series|docpage|volume|journal|publisher|isbn|lang|annote|edition|shortin|isbn13|location|school|superviser|address))',
        r'},\n\1',
        docBib
    )

    docBib = re.sub(
        r',}',
        r',\n}',
        docBib
    )

    # newlines para categoria
    docBib = re.sub(
        r'@',
        r'\n@',
        docBib
    )

    docBib = re.sub(
        r'(@[^,]+,)',
        r'\1\n',
        docBib
    )


    # Escape character
    docBib = re.sub(
        r'\\',
        r'\\\\',
        docBib
    )

    # Remove all lines but author
    docBib = re.sub(
        r'(?i)^((?!\bauthor\b).)*$\n',
        r'',
        docBib,
        flags=re.M #Multiline
    )
    
    #Arranjar espaços
    docBib = re.sub(
        r' +',
        r' ',
        docBib
    )

    #Remover double And
    docBib = re.sub(
        r'and and',
        r'and',
        docBib
    )


    #Limpar special chars
    docBib = re.sub(
        r'\\\\[\'\~]',
        r'',
        docBib
    )

    #Limpar special chars
    docBib = re.sub(
        r'[\{\}]',
        r'"',
        docBib
    )

    #Limpar ,
    docBib = re.sub(
        r'\",',
        r'"',
        docBib
    )

    #Remove ""
    docBib = re.sub(
        r'\"\"',
        r'"',
        docBib
    )

    #Remove projecto
    docBib = re.sub(
        r'projecto ',
        r'',
        docBib
    )

    #remove author
    docBib = re.sub(
        r'(?i) *author *= *',
        r'',
        docBib
    )

    #remove "
    docBib = re.sub(
        r'\"',
        r'',
        docBib
    )

#### Fix Names
    docBib = re.sub(
        r'( and|\n) ?(\w+), (\w+)( and |\n)',
        r'\1 \3 \2\4',
        docBib
    )

    docBib = re.sub(
        r'( and|\n) ?(\w+), (\w+)( and |\n)',
        r'\1 \3 \2\4',
        docBib
    )

    docBib = re.sub(
        r' *(\w+), (\w\.\w\.)( and|\n)',
        r' \2 \1\3',
        docBib
    )

    docBib = re.sub(
        r'( and|\n)( ?\w+),( ?\w+)( \w+)( and |\n)',
        r'\1\3\4\2\5',
        docBib
    )

    docBib = re.sub(
        r'( and|\n)( \w+)( \w+),( \w+)( and|\n)',
        r'\1\4\2\3\5',
        docBib
    )

    docBib = re.sub(
        r'( and|\n) ?( \w+),( \w+)( \w+ã)(\w+)( \w+)( and|\n)',
        r'\1\3\4\5\6\2\7',
        docBib
    )

    # remove space before '
    docBib = re.sub(
        r' \'',
        r'\n',
        docBib
    )

    # remove space after \n
    docBib = re.sub(
        r'\n *',
        r'\n',
        docBib
    )

    # remove space before \n
    docBib = re.sub(
        r' *\n',
        r'\n',
        docBib
    )

    authors = {}

    for line in docBib.splitlines():
        res = re.split(
            r' *\band\b *',
            line
            )
        for elem in res:
            for value in res:
                if value != elem:
                    authors.setdefault(elem, set()).add(value)
    return authors.get(author)


with open("Trabalho/exemplo-utf8.bib", encoding="utf8") as f:
    val = input("Enter the author: ")
    conteudo = f.read()
    lista = worker(conteudo,val)
    out = open ("Trabalho/outD.txt","w")
    for elem in lista:
        out.write(elem+"\n")

    dot = Digraph()
    dot.node(val,val)
    for elem in lista:
        dot.node(elem,elem)
        dot.edge(val,elem)
    dot.render('Trabalho/grafo.gv', view=False) 

# L.S. Barbosa
# J.J. Almeida

    