import calculator1 as c

my_calc=c.Calculator()

loop =True

while loop:
    print("Insert the operator:")
    print("+ : Adiction")
    print("- : Subtration")
    print("x : Multiply")
    print("/ : Division")
    print("T : terminate")

    option = input("Option: ")

    if option in("+","-","x","/","T"):
        if option == "T":
            loop = False
        
        else: 
            a = int (input("Insert the 1º number:"))
            b = int (input("Insert the 2º number:"))
            
            if option=="+":
                res= my_calc.add(a,b)
            if option=="-":
                res= my_calc.sub(a,b)
            if option=="x":
                res= my_calc.mul(a,b)
            if option=="/":
                res= my_calc.div(a,b)
            
            print(res)

        print("Option Invalad")



