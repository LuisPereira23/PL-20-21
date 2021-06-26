import re

def bibtex2json(docBib):
    #abrir lista
    docBib = "[" + docBib

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

    out = open ("1.bib","w")
    out.write(docBib)

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

    # Adicionar , para manter lista
    docBib = re.sub(
        r'}\n',
        r'},\n',
        docBib
    )

    #Remover trailing Commas 
    docBib = re.sub(
        r',\n}',
        r'\n}',
        docBib
    )

    out = open ("2.bib","w")
    out.write(docBib)

    docBib = re.sub(
        r'@([a-zA-z]+){([À-ÿa-zA-Z0-9 :,\\{}/\.\-]+),',
        r'{\n\t"categoria":"\1",\n\t"label":"\2",',
        docBib
    )

    docBib = re.sub(
        r'(?i) *(author|title|note|booktitle|year|institution|type|keyword|editor|url|month|abstract|pages|number|series|docpage|volume|journal|publisher|isbn|lang|annote|edition|shortin|isbn13|location|school|superviser|address) *=\t? *[\"{](.*)[\"}]',
        r'\t"\1":"\2"',
        docBib
    )

    #Arranjar espaços
    docBib = re.sub(
        r' +',
        r' ',
        docBib
    )
    

    docBib = docBib + "]"

    #remove last comma
    docBib = re.sub(
        r',\n]',
        r'\n]',
        docBib
    )

    return docBib






with open("exemplo-utf8.bib", encoding="utf8") as f:
    out = open ("test.json","w")
    conteudo = f.read()
    out.write(bibtex2json(conteudo))

    