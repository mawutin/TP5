#coding:utf-8
import math

a=float(input("entrer un nombre reel a="))
b=float(input("entrer un nombre reel b="))
c=float(input("entrer un nombre reel c="))

D=b**2 - 4*a*c

if a==0:
    print("Le polynôme n\'est pas du second degré")
else:
    if(D == 0):
        x0=-b/(2*a)
        print()
    elif D < 0 :
        print("L\'équation n\'admet pas de solution")
    else:
        x1=(-b+math.sqrt(D))/2*a
        x2=(-b-math.sqrt(D))/2*a
        print("L\'équation admet udeux solutions qui sont x1,x2")
        print("x1= ",x1, "x2= ",x2)
