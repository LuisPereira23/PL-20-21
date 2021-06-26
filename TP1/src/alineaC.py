import re

def bibtex2json(docBib):

    docBib = "[" + docBib

    docBib = re.sub(
        r',\n',
        r',',
        docBib
    )

    docBib = re.sub(
        r'["}],',
        r',\n',
        docBib
    )

    docBib = re.sub(
        r'@',
        r'\n@',
        docBib
    )


    docBib = re.sub(
        r'%(.)*',
        r'',
        docBib
    )

    docBib = re.sub(
        r'>.*\n+',
        r'',
        docBib
    )

    docBib = re.sub(
        r'@([a-zA-z]+){([À-ÿa-zA-Z0-9 :,\\{}/\.\-]+),',
        r'{\n\t"categoria":"\1",\n\t"label":"\2",',
        docBib
    )

    docBib = re.sub(
        r'(?i) +author *= *{([À-ÿa-zA-Z0-9 ,\\{}:/\.\'\~]+)\n? *([À-ÿa-zA-Z0-9 ,\\{}:/\.]*)}',
        r'\t"author":"\1 \2"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +author *= *\"([À-ÿa-zA-Z0-9 ,\\{}:/\.]+)\n? *([À-ÿa-zA-Z0-9 ,\\{}:/\.]*)\"',
        r'\t"author":"\1 \2"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +title *= *{([À-ÿa-zA-Z0-9 ,\{\}\+\=\!:\/\.\?\_\$\-\&\'\(\)\{\}\#\\]+)\n?( *[À-ÿa-zA-Z0-9 ,\{\}:\/\.\-*]*)\n?( *[À-ÿa-zA-Z0-9 ,\{\}:\/\.]*)}',
        r'\t"title":"\1\2\3"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +title *= *{([^"]+)\n?("(.*)")( *[À-ÿa-zA-Z0-9 ,\\{}:\/\.\-*]*)\n?( *[À-ÿa-zA-Z0-9 ,\\{}:\/\.]*)}',
        r'\t"title":"\1\3\4"',
        docBib
    )


    docBib = re.sub(
        r' +title *= *\"([À-ÿa-zA-Z0-9 \=\,\{\}\!:\/\.\?\\]+)\n?( *[À-ÿa-zA-Z0-9 \,\{\}:\/\.\-\*]*)\n?( *[À-ÿa-zA-Z0-9 \,\{\}\:\/\.]*)\"',
        r'\t"title":"\1\2\3"',
        docBib
    )

    docBib = re.sub(
        r' +note *= *\"([À-ÿa-zA-Z0-9 ,\\{}:/\.]+)\n? *([À-ÿa-zA-Z0-9 ,\\{}:/\.]*)\"',
        r'\t"note":"\1\2"',
        docBib
    )


    docBib = re.sub(
        r' +note *= *{([^}]*) *}',
        r'\t"note":"\1"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +booktitle *= *{([\$\º\'\ª\-À-ÿa-zA-Z0-9 ,\\{}:/\(\)\.]+)\n? *([À-ÿa-zA-Z0-9 ,\\{}:/\(\)\.]*)}',
        r'\t"booktitle":"\1 \2"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +booktitle *= *\"([\'\-À-ÿa-zA-Z0-9 ,\\{}:/\(\)\.]+)\n? *([À-ÿa-zA-Z0-9 ,\\{}:/\(\)\.]*)\"',
        r'\t"booktitle":"\1 \2"',
        docBib
    )

    docBib = re.sub(
        r' +address *= *\"([^\"]+)\"',
        r'\t"adress":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +address *= *{(.*) *}',
        r'\t"address":"\1"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +year *= *([0-9]+)',
        r'\t"year":"\1"',
        docBib
    )
    docBib = re.sub(
        r'(?i) +year *= *\"([0-9]+)\"',
        r'\t"year":"\1"',
        docBib
    )
    docBib = re.sub(
        r'(?i) +year *= *{([0-9]*)}',
        r'\t"year":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +institution *= *\"(.*) *\"',
        r'\t"institution":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +type *= *\"(.*) *\"',
        r'\t"type":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +keyword *= *\"(.*) *\"',
        r'\t"keyword":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +keyword *= *{(.*) *}',
        r'\t"keyword":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +editor *=\t* *{(.*) *}',
        r'\t"editor":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +url *= *\"(.*) *\"',
        r'\t"url":"\1"',
        docBib
    )

    docBib = re.sub(
        r' *url *=\n? *{(.*) *}',
        r'\t"url":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +month *= *\"(.*) *\"',
        r'\t"month":"\1"',
        docBib
    )
    docBib = re.sub(
        r' +month *= *{(.*) *}',
        r'\t"month":"\1"',
        docBib
    )
#
#    docBib = re.sub(
#        r' +abstract *= *{([0-9]*)}',
#        r'\t"abstract":"\1"',
#        docBib
#    )
#
#    docBib = re.sub(
#        r' +abstract *= *\"([0-9]*)\"',
#        r'\t"abstract":"\1"',
#        docBib
#    )

    docBib = re.sub(
        r' +editor *= *\"(.+) *\"',
        r'\t"editor":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +pages *= *\"(.*) *\"',
        r'\t"pages":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +pages *=\t* *{(.*) *}',
        r'\t"pages":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +number *= *[\"{](.*) *[\"}]',
        r'\t"number":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +number *= *\"?([0-9]*)\"?',
        r'\t"number":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +note *= *\"(.+) *\"',
        r'\t"note":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +publisher *= *\"(.*) *\"',
        r'\t"publisher":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +publisher *= *{(.*) *}',
        r'\t"publisher":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +docpage *= *\"(.+) *\"',
        r'\t"docpage":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +series *= *\"(.+) *\"',
        r'\t"series":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +series *=\t* *{(.+) *}',
        r'\t"series":"\1"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +volume *= *\"([0-9]*)\"',
        r'\t"volume":"\1"',
        docBib
    )

    docBib = re.sub(
        r'(?i) +volume *=\t* *{?([0-9A-Z\(\) ]*)}?',
        r'\t"volume":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +journal *= *{(.+) *}',
        r'\t"journal":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +journal *= *\"(.+) *\"',
        r'\t"journal":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +isbn *= *\"(.*) *\"',
        r'\t"isbn":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +(isbn|ISBN)(13)? *= *{(.*) *}',
        r'\t"\1\2":"\3"',
        docBib
    )

    docBib = re.sub(
        r' +lang *= *\"(.*) *\"',
        r'\t"lang":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +lang *= *{(.*) *}',
        r'\t"lang":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +school *= *{(.+) *}',
        r'\t"school":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +superviser *= *\"(.*) *\"',
        r'\t"superviser":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +location *= *\"(.*) *\"',
        r'\t"location":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +Note *= *\"(.*) *\"',
        r'\t"note":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +shortin *= *{(.*) *}',
        r'\t"shortin":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +edition *=\t* *{(.*) *}',
        r'\t"edition":"\1"',
        docBib
    )

    docBib = re.sub(
        r' +annote *=\t* *{(.*) *}',
        r'\t"annote":"\1"',
        docBib
    )


    docBib = re.sub(
        r'\\',
        r'\\\\',
        docBib
    )


    docBib = re.sub(
        r'}\n',
        r'},\n',
        docBib
    )

    docBib = re.sub(
        r',\n}',
        r'\n}',
        docBib
    )
    
    

    docBib = docBib + "]"
    return docBib






with open("exemplo-utf8.bib", encoding="utf8") as f:
    out = open ("out.json","w")
    conteudo = f.read()
    out.write(bibtex2json(conteudo))

    