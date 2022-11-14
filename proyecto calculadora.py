
'''
S:SUMA
R:RESTA
M:MULTIPLICACION
D:DIVISION
'''


def SUMA():
    num1=input("ingrese un numero:")
    num2= input("ingrese otro numero:")
    print(num1,"+", num2,"=", num1+ num2)

def RESTA():
    num1=input("ingrese un numero:")
    num2= input("ingrese otro numero:")
    print(num1,"-", num2,"=", num1-num2)
  
def MULTIPLICACION():
    num1=input("ingrese un numero:")
    num2= input("ingrese otro numero:")
    print(num1,"*", num2,"=", num1*num2)    

def DIVISION():
    num1=input("ingrese un numero:")
    num2= input("ingrese otro numero:")
    print(num1,"/", num2,"=", num1/num2)  
    

input('Bienvenido') 
while True:      
    Operacion= int (input())
    if  Operacion=="SUMA " :
        SUMA()
    elif Operacion=="RESTA" :  
        RESTA()
    elif Operacion== "MULTIPLICACION":
        MULTIPLICACION()
    elif Operacion== "DIVISON":
        DIVISION()


