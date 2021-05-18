a = int (input("Insert the 1º number:"))
b = int (input("Insert the 2º number:"))
op =input("Insert the operator:")

if op=="+":
    res=a+b
elif op=="-":
    res=a-b
elif op=="x":
    res= a*b
elif op=="/":
    res= a/b
else: res= "invalad operation"

print(res)