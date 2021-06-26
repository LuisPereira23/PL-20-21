import ply.yacc as yacc
import sys
from TP2_lex import tokens
from TP2_lex import literals

operacoes = {'+':'ADD','*':'MUL','/':'DIV','-':'SUB','mod':'MOD','==':'EQUAL','<':'INF','<=':'INFEQ','>':'SUP','>=':'SUPEQ'}

def p_Call(p):
    "Call : Elementos RUN '(' ')'"
    f.write(p[1])
    while p.parser.registers.get("varCount") > 0:
        line_prepender("PUSHI 0\n")
        p.parser.registers.update({"varCount" : p.parser.registers.get("varCount") -1})
    if( p.parser.registers.get("arrayCount") >0):
        line_prepender("PUSHN "+ str(p.parser.registers.get("arrayCount")) )


def p_Elementos(p):
    "Elementos : Elementos Elemento "
    p[0] = p[1] + p[2]
    

def p_Elementos_vazio(p):
    "Elementos : "
    p[0]= ""

def p_Elemento_OperAr(p):
    "Elemento : OperAr"
    p[0]=p[1]

def p_Elemento_OperLog(p):
    "Elemento : OperLog"
    p[0]=p[1]

def p_Elemento_OperRel(p):
    "Elemento : OperRel"
    p[0]=p[1]

def p_Elemento_Atri(p):
    "Elemento : Atri"
    p[0]=p[1]

def p_Return(p):
    "Elemento : RETURN Var"
    p[0]= ("PUSHG " + str(p.parser.registers.get(p[2])) + "\n")

def p_Elemento_Funcao(p):
    "Elemento : Funcao "
    p[0]=p[1]

def p_Elemento_Io(p):
    "Elemento : Io "
    p[0]=p[1]

def p_Elemento_Conditional(p):
    "Elemento : Conditional "
    p[0]=p[1]

def p_Elemento_For(p):
    "Elemento : For  fimFor fimFor2 "
    p[0]=p[1] + p[3] + p[2]

def p_For(p):
    "For : FOR '(' Atri ';' OperRel  "

    p[0] = p[3] +("FOR"+str(p.parser.registers.get("for"))+":\n")+ p[5]  + ("JZ fimFOR"+str(p.parser.registers.get("for2"))+"\n")
    p.parser.registers.update({"for": (p.parser.registers.get("for")+1) })

def p_fimFor(p):
    "fimFor : ';' Atri ')'  "
    p[0] = p[2] + ("JUMP FOR"+str(p.parser.registers.get("for3"))+"\n") + ("fimFOR"+str(p.parser.registers.get("for2"))+":\n")
    p.parser.registers.update({"for2": (p.parser.registers.get("for2")+1) })
    p.parser.registers.update({"for3": (p.parser.registers.get("for3")+1) })
    
def p_fimFor2(p):
    "fimFor2 : '{' Elementos  '}'"
    p[0] = p[2]
    


def p_Conditional_Else(p):
    "Conditional : inicioElse fimElse"
    p[0] = p[1]+p[2]

def p_Conditional_inicioElse(p):
    "inicioElse : ELSE "
    p[0]= ("ELSE"+str(p.parser.registers.get("contador2"))+":\n") 
    

def p_Conditional_fimElse(p):
    "fimElse : '{' Elementos '}' "
    p.parser.registers.update({"contador2": (p.parser.registers.get("contador2")+1) })
    p[0]=p[2]+("fimIF"+str(p.parser.registers.get("contador5"))+":\n")
    p.parser.registers.update({"contador5": (p.parser.registers.get("contador5")+1) })
    

def p_Conditional_IF(p):
    "Conditional : inicioIF fimIF"
    p[0] = p[1]+p[2]

def p_Conditional_fimIf(p):
    "fimIF :  '{' Elementos '}' "
    p[0] = p[2]+("JUMP fimIF"+str(p.parser.registers.get("contador4"))+"\n")
    p.parser.registers.update({"contador4": (p.parser.registers.get("contador4")+1) })
    
    

def p_Inicio_If_Oper(p):
    "inicioIF : IF '(' OperRel ')' "
    p[0] = p[3] + ("JZ ELSE"+str(p.parser.registers.get("contador"))+"\n")
    p.parser.registers.update({"contador": (p.parser.registers.get("contador")+1) })

def p_Inicio_If_Log(p):
    "inicioIF : IF '(' Var ')' "
    p[0] = ("PUSHI "+str(p.parser.registers.get(p[3]))+"\n")+("JZ ELSE"+str(p.parser.registers.get("contador"))+"\n")
    p.parser.registers.update({"contador": (p.parser.registers.get("contador")+1) })
 

def p_Funcao(p):
    "Funcao : FNAM '(' ')' '{' Elementos '}'"
    p[0]= p[5]

def p_Array(p):
    "Atri : VAR '[' NUM ']'"
    if p[1] not in p.parser.registers:
        p.parser.registers.update({"arrayCount" : p.parser.registers.get("arrayCount") + int(p[3])})
        p.parser.registers.update({p[1]: (p.parser.registers.get("offset")) })
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+int(p[3])) })
    p[0] = ""
    

def p_Atri_Array_NUM(p):
    "Atri : VAR '[' NUM ']' '=' NUM"
    p[0] =  "PUSHGP\n" + "PUSHI " + str(p.parser.registers.get(p[1])) +"\n" + "PADD\n" + "PUSHI " + p[3] + "\n" + "PUSHI " + p[6] + "\n" + "STOREN\n" 

def p_Atri_Array_Var(p):
    "Atri : VAR '[' NUM ']' '=' VAR"
    p[0] =  "PUSHGP\n" + "PUSHI " + str(p.parser.registers.get(p[1])) +"\n" + "PADD\n" + "PUSHI " + p[3] + "\n" + "PUSHG " + str(p.parser.registers.get(p[6])) + "\n" + "STOREN\n" 

def p_Atri_Array_Var_NUM(p):
    "Atri : VAR '[' Var ']' '=' NUM"
    p[0] =  "PUSHGP\n" + "PUSHI " + str(p.parser.registers.get(p[1])) +"\n" + "PADD\n" + "PUSHG " + str(p.parser.registers.get(p[3])) + "\n" + "PUSHI " + p[6] + "\n" + "STOREN\n" 

def p_Atri_Array_Var_Var(p):
    "Atri : VAR '[' Var ']' '=' VAR"
    p[0] =  "PUSHGP\n" + "PUSHI " + str(p.parser.registers.get(p[1])) +"\n" + "PADD\n" + "PUSHG " + str(p.parser.registers.get(p[3])) + "\n" + "PUSHG " + str(p.parser.registers.get(p[6])) + "\n" + "STOREN\n" 


def p_Atri_Var_Array(p):
    "Atri : INT Var '=' VAR '[' Var ']'"

    if p[2] in p.parser.registers:
        p[0] =  "PUSHGP\n" + "PUSHI " + str(p.parser.registers.get(p[4])) +"\n" + "PADD\n" + "PUSHG " + str(p.parser.registers.get(p[6])) + "\n" + "LOADN\n"  + ("STOREG " + str(p.parser.registers.get(p[2]))+"\n")  
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0] =  "PUSHGP\n" + "PUSHI " + str(p.parser.registers.get(p[4])) +"\n" + "PADD\n" + "PUSHG " + str(p.parser.registers.get(p[6])) + "\n" + "LOADN\n"  + ("STOREG " + str(p.parser.registers.get(p[2]))+"\n") 
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })


def p_Atri_Funcao(p):
    "Atri : INT Var '=' Funcao "
    if p[2] in p.parser.registers:
        p[0] = p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0] = p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Atri_Exp(p):
    "Atri : INT Var '=' OperAr"

    if p[2] in p.parser.registers:
        p[0] = p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0] = p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Atri_Simple(p):
    "Atri : INT Var '=' NUM"
    if p[2] in p.parser.registers:
        p[0] = ("PUSHI " +p[4]+"\n") + ("STOREG " + str(p.parser.registers.get(p[2]))+"\n") 
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0] = ("PUSHI " +p[4]+"\n") + ("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Atri_Log_Oper(p):
    "Atri : BOOLEAN Var '=' OperLog"
    if p[2] in p.parser.registers:
        p[0]= p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n") 
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0]=p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Atri_Rel_Oper(p):
    "Atri : BOOLEAN Var '=' OperRel"
    if p[2] in p.parser.registers:
        p[0]= p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n") 
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0]=p[4]+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Atri_Log(p):
    "Atri : BOOLEAN Var '=' BOOL"
    if(p[4]=="True"):
        bol = "1"
    else:
        bol = "0"

    if p[2] in p.parser.registers:
        p[0] = ("PUSHI "+bol+"\n")+("STOREG " + str(p.parser.registers.get(p[2]))+"\n") 
        
    else:
        p.parser.registers.update({p[2]:p.parser.registers.get("offset")})
        p[0] = ("PUSHI "+bol+"\n")+("STOREG " + str(p.parser.registers.get(p[2]))+"\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Io_Read_Int(p):
    "Io : READ '(' Var ')'"
    if p[3] in p.parser.registers:
        p[0] = ('READ\nATOI\n')  + ("STOREG ") + (str(p.parser.registers.get(p[3])) + "\n")
        
    else:
        p.parser.registers.update({p[3]:p.parser.registers.get("offset")})
        p[0] = ('READ\nATOI\n')  + ("STOREG ") + (str(p.parser.registers.get(p[3])) + "\n")
        p.parser.registers.update({"offset": (p.parser.registers.get("offset")+1) })

def p_Io_Write_Int(p):
    "Io : WRITE NUM"
    p[0] = ("PUSHI "+p[2]+"\n")+('WRITEI\n')

def p_Io_Write_Var(p):
    "Io : WRITE Var"
    p[0] = ("PUSHG " + str(p.parser.registers.get(p[2])) + "\n") + ('WRITEI\n')

def p_Io_Write_String(p):
    "Io : WRITE '(' TEXTO ')' "
    p[0] = ("PUSHS "+p[3]+"\n")+('WRITES\n')

def p_Oper_AND_Bool(p):
    "OperLog : BOOL AND BOOL"
    if(p[1]=="True"):
        bol = "1"
    else:
        bol = "0"

    if(p[3]=="True"):
        bol2 = "1"
    else:
        bol2 = "0"

    p[0] = ("PUSHI "+bol+"\n")+("PUSHI "+bol2+"\n")+(operacoes.get("*")+"\n")

def p_Oper_AND_Var(p):
    "OperLog : Var AND Var"
    p[0] = ("PUSHG " + str(p.parser.registers.get(p[1])) + "\n")+("PUSHG " + str(p.parser.registers.get(p[3])) + "\n")+(operacoes.get("*")+"\n")

def p_Oper_AND_Var_BOOLEAN(p):
    "OperLog : Var AND BOOL"
    if(p[3]=="True"):
        bol = "1"
    else:
        bol = "0"
    p[0]=("PUSHG " + str(p.parser.registers.get(p[1])) + "\n")+("PUSHI "+bol+"\n")+(operacoes.get("*")+"\n")

def p_Oper_AND_BOOLEAN_Var(p):
    "OperLog : BOOL AND Var"
    if(p[1]=="True"):
        bol = "1"
    else:
        bol = "0"
    p[0]= ("PUSHI "+bol+"\n")+("PUSHG " + str(p.parser.registers.get(p[3])) + "\n")+(operacoes.get("*")+"\n")

def p_Oper_OR_BOOLEAN(p):
    "OperLog : BOOL OR BOOL"
    if(p[1]=="True"):
        bol = "1"
    else:
        bol = "0"

    if(p[3]=="True"):
        bol2 = "1"
    else:
        bol2 = "0"

    p[0] = ("PUSHI "+bol+"\n")+("PUSHI "+bol2+"\n")+(operacoes.get("+")+"\n")+("PUSHI "+bol+"\n")+("PUSHI "+bol2+"\n")+(operacoes.get("*")+"\n")+(operacoes.get("-")+"\n")


def p_Oper_OR_Var(p):
    "OperLog : Var OR Var"
    p[0] =("PUSHG " + str(p.parser.registers.get(p[1])) + "\n")+("PUSHG " + str(p.parser.registers.get(p[3])) + "\n")+(operacoes.get("+")+"\n")+("PUSHG " + str(p.parser.registers.get(p[1])) + "\n")+("PUSHG " + str(p.parser.registers.get(p[3])) + "\n")+(operacoes.get("*")+"\n")+(operacoes.get("-")+"\n")


def p_Oper_OR_Var_Bool(p):
    "OperLog : Var OR BOOL"

    if(p[3]=="True"):
        bol = "1"
    else:
        bol = "0"

    p[0] = ("PUSHG " + str(p.parser.registers.get(p[1])) + "\n")+("PUSHI "+bol+"\n")+(operacoes.get("+")+"\n")+("PUSHG " + str(p.parser.registers.get(p[1])) + "\n")+("PUSHI "+bol+"\n")+(operacoes.get("*")+"\n")+(operacoes.get("-")+"\n")


def p_Oper_OR_Bool_Var(p):
    "OperLog : BOOL OR Var"
    if(p[1]=="True"):
        bol = "1"
    else:
        bol = "0"
    p[0]= ("PUSHI "+bol+"\n")+("PUSHG " + str(p.parser.registers.get(p[3])) + "\n")+(operacoes.get("+")+"\n")+("PUSHI "+bol+"\n")+("PUSHG " + str(p.parser.registers.get(p[3])) + "\n")+(operacoes.get("*")+"\n")+(operacoes.get("-")+"\n")


def p_Oper_add(p):
    "OperAr : OperAr '+' Termo"
    p[0]= p[1] + p[3] + "ADD\n"

def p_Oper_sub(p):
    "OperAr : OperAr '-' Termo"
    p[0]= p[1] + p[3] + "SUB\n"

def p_Oper_termo(p):
    "OperAr : Termo"
    p[0]=p[1]

def p_Oper_mul(p):
    "Termo : Termo '*' Factor"

    p[0]= p[1] + p[3] + "MUL\n"

def p_Termo_div(p):
    "Termo : Termo '/' Factor"
    p[0]= p[1] + p[3] + "DIV\n"

def p_Termo_mod(p):
    "Termo : Termo MOD Factor"
    p[0]= p[1] + p[3] + "MOD\n"
    
def p_Termo_factor(p):
    "Termo : Factor"
    p[0]=p[1]

def p_Factor_group(p):
    "Factor : '(' OperAr ')'"
    p[0]= p[2]

def p_Factor_num(p):
    "Factor : NUM"
    p[0] = "PUSHI "+p[1]+"\n"

def p_Factor_id(p):
    "Factor : Var"
    p[0] = "PUSHG "+str(p.parser.registers.get(p[1])) + "\n"


def p_Oper_Rel_Equal(p):
    "OperRel : Factor EQUALS Factor"
    p[0] = p[1] + p[3] + "EQUAL\n"

def p_Oper_Rel_Inf(p):
    "OperRel : Factor INF Factor"
    p[0] = p[1] + p[3] + "INF\n"

def p_Oper_Rel_Sup(p):
    "OperRel : Factor SUP Factor"
    p[0] = p[1] + p[3] + "SUP\n"

def p_Oper_Rel_InfEQ(p):
    "OperRel : Factor INFEQ Factor"
    p[0] = p[1] + p[3] + "INFEQ\n"

def p_Oper_Rel_SupEQ(p):
    "OperRel : Factor SUPEQ Factor"
    p[0] = p[1] + p[3] + "SUPEQ\n"
   
def p_Var(p):
    "Var : VAR"
    if p[1] not in p.parser.registers:
        p.parser.registers.update({"varCount" : p.parser.registers.get("varCount") +1})
    p[0] = p[1]

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

parser = yacc.yacc()
parser.registers = {}
parser.registers.update({"offset":0})
parser.registers.update({"contador":0})
parser.registers.update({"contador2":0})
parser.registers.update({"contador3":0})
parser.registers.update({"contador4":0})
parser.registers.update({"contador5":0})
parser.registers.update({"for":0})
parser.registers.update({"for2":0})
parser.registers.update({"for3":0})
parser.registers.update({"varCount":0})
parser.registers.update({"arrayCount":0})

import sys

def line_prepender(line):
    with open("demofile.vm", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

with open("/home/krow/Documents/PL/Trabalho2.2/testArray.py", 'r') as file:
    data = file.read()

f = open("demofile.vm", "w")
f.write("START\n")
f.close()
f = open("demofile.vm", "a")

parser.success = True
parser.parse(data)


if parser.success:
    f.write("Fim: stop\n")
    f.close()
    print("Sintaxe reconhecida: ", data)

else:
    print("Erro de sintaxe")

