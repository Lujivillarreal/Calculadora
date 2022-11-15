operacion= "SUMAR","RESTA","MULTIPLICAR","DIVIDIR"
a="SUMAR"
b="RESTAR"
c="MULTIPLICAR"
d="DIVIDIR"

input('Bienvenido')
num1=input("ingrese un numero:")
num2= input("ingrese otro numero:") 
print ("indique la operacion que desea realizar: ")
print("a=>SUMAR")
print("b=>RESTAR") 
print("c=>MULTIPLICAR")    
print("d=>DIVIDIR")    
operacion= input("indique la operacion que desea realizar: ")
if operacion=="a" :
    print(num1,"+",num2,"=", num1+num2)
elif operacion=="b" :  
    print(num1,"-",num2, "=", int(num1)- int (num2))
elif operacion== "c":
    print(num1,"x",num2,"=", int(num1)*int(num2))
elif operacion== "d":
    print(num1,"/",num2,"=", int(num1)/int(num2))





