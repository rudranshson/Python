#i am creating the calculator and this is my first project

def add(a,b):
    return a+b

def sub(c,d):
    return c-d

def multi(q,w):
    return q*w


def divi(e,r):
    if r == 0 :
        return ("error :the number cannot be divided by 0")

    
    return e/r


Equat= input("enter the values you want to calculate:")
Equat= Equat.replace('+',' + ')
Equat= Equat.replace('-',' - ')
Equat= Equat.replace('/',' / ')
Equat= Equat.replace('*',' * ')
print(f"the equatin is being solved please wait a whil {Equat} ")


equation_c= Equat.split()

i=0
while i < len(equation_c):
    if equation_c[i]== '*' :
        num1 = float(equation_c[i-1])
        num2 = float(equation_c[i+1])

        ans=multi(num1,num2)

        equation_c.pop(i-1)
        equation_c.pop(i-1)
        equation_c.pop(i-1)

        equation_c.insert(i-1,str(ans))
        i=max(i-1,0)
    elif equation_c[i]== '/' :
        num1 = float(equation_c[i-1])
        num2 = float(equation_c[i+1])

        ans=divi(num1,num2)  
        equation_c.pop(i-1)
        equation_c.pop(i-1)
        equation_c.pop(i-1)

        equation_c.insert(i-1,str(ans))
        i=max(i-1,0)
    else:
        i+=1




i=0
while i < len(equation_c):
    if equation_c[i]== '+' :
        num1 = float(equation_c[i-1])
        num2 = float(equation_c[i+1])

        ans=add(num1,num2)  
        equation_c.pop(i-1)
        equation_c.pop(i-1)
        equation_c.pop(i-1)

        equation_c.insert(i-1,str(ans))
        i=max(i-1,0)
    elif equation_c[i]== '-' :
        num1 = float(equation_c[i-1])
        num2 = float(equation_c[i+1])

        ans=sub(num1,num2)  
        equation_c.pop(i-1)
        equation_c.pop(i-1)
        equation_c.pop(i-1)
        equation_c.insert(i-1,str(ans))
        i=max(i-1,0)
    else :
        i+=1


print(f"result:{equation_c[0]}")
    

                                








   

    
