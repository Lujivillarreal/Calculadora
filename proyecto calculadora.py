operacion= "SUMAR","RESTA","MULTIPLICAR","DIVIDIR"
SUMAR="a"
RESTAR="b"
MULTIPLICAR= "c"
DIVIDIR= "d"

input('Bienvenido')
num1=input("ingrese un numero:")
num2= input("ingrese otro numero:") 
print ("indique la operacion que desea realizar: ")
print("a=>SUMAR")
print("b=>RESTAR") 
print("c=>MULTIPLICAR")    
print("d=>DIVIDIR")    
operacion= input("indique la operacion que desea realizar: ")
if operacion=="SUMAR" :
    print(num1,"+",num2,"=", num1+num2)
elif operacion=="RESTAR" :  
    print(num1,"-",num2, "=", int(num1)- int (num2))
elif operacion== "MULTIPLICAR":
    print(num1,"x",num2,"=", int(num1)*int(num2))
elif operacion== "DIVIDIR":
    print(num1,"/",num2,"=", int(num1)/int(num2))





