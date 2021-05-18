def str_nrs(v1,op,v2,res):
    return str(v1) + op +str(v2) + "=" + str(res)

class Calculator:
    def add(self,a,b):
        res =a+b
        return res ,str_nrs(a, '+', b, res)
    def sub(self,a,b):
        res = a-b
        return res ,str_nrs(a, '-', b, res)
    def mul(self,a,b):
        res = a*b
        return res ,str_nrs(a, 'x', b, res)
    def div(self,a,b):
        if b== 0:
            raise ValueError("Division by zero!")
            ##raise ZeroDivisionError()
            ##raise TypeError() #if you want to show a error
        else:
            res= a/b
            return res ,str_nrs(a, '/', b, res)