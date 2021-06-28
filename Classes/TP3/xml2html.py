# Conversão dum relatório XML para uma página HTML



import re



def xml2html(docXML):

    declXML = re.search(r'<\?[^?]+\?>', docXML).group()

    encoding = re.search(r'encoding\s*=\s*(\"[^"]+\")', declXML).group(1)

    

    docHTML = re.sub(

        r'<\?[^?]+\?>',

        rf'''<!DOCTYPE html>

<html>

    <head>

        <title>Relatório</title>

        <meta charset={encoding}/>

    </head>''',

        docXML

    )



    docHTML = re.sub(

        r'<relatorio>((.|\n)*)<\/relatorio>',

        r'<body>\n\1\n</body>\n</html>',

        docHTML

    )



    docHTML = re.sub(

        r'<titulo>((.|\n)*)<\/titulo>',

        r'<h1>\1</h1>',

        docHTML

    )



    docHTML = re.sub(

        r'<data>((.|\n)*)<\/data>',

        r'<h2>\1</h2>',

        docHTML

    )



    docHTML = re.sub(

        r'<autores>((.|\n)*)<\/autores>',

        r'<h3>Autores</h3>\n<ul>\1</ul>',

        docHTML

    )



    while re.search(r'<autor>((.|\n)*?)<\/autor>', docHTML):

        docHTML = re.sub(

        r'<autor>( |\n)*<nome>([a-zA-Z ]+)<\/nome>( |\n)*<numero>([A-Z0-9]+)<\/numero>( |\n)*<email>([^<]+)<\/email>( |\n)*<\/autor>',

        rf'<li>\2(\4): \6</li>',

        docHTML

        )



        docHTML = re.sub(

        r'<autor>( |\n)*<nome>([a-zA-Z ]+)<\/nome>( |\n)*<email>([^<]+)<\/email>( |\n)*<\/autor>',

        rf'<li>\2: \4</li>',

        docHTML

        )



    docHTML = re.sub(

        r'<descricao>((.|\n)*)<\/descricao>',   

        r'<h3>Resumo</h3>\n<p>\1</p>',

        docHTML

    )



    print(docHTML)







with open("relatorio.xml") as f:

    conteudo = f.read()

    xml2html(conteudo)