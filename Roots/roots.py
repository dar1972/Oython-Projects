import math

"""
This function first calculates the value of the discriminate and checks whether the d is less than, equal to or more than 0
then it calculates the roots of the equation according to the value of d
"""
def calculate_roots(a,b,c):
    d=(b**2)-(4*a*c)
    if d > 0:
        print("Equation:",a,"x^2 + ",b ,"x + ", c, sep="")
        print ("2 roots")
        print("This equation has two solutions: ",(-b+math.sqrt(d))/(2*a), " and",  (-b-math.sqrt(d))/(2*a))
    elif d==0:
        print("Equation:",a,"x^2 + ",b ,"x + ", c, sep="")
        print("only one root")
        print("x =", (-b/(2*a)))
    elif d < 0:
        print("Equation:",a,"x^2 + ",b ,"x + ", c, sep="")
        print(" no roots exits")
    
"""
Putting 10 random values in the function and calls it
"""
computing_roots(3,-20,7)
computing_roots(-1,3,7)
computing_roots(0,0,0)
computing_roots(7,11,4)
computing_roots(7,8,1)
computing_roots(1,1,9)
computing_roots(9,0.3,4.1)
computing_roots(9,1,1)
computing_roots(9.11,1.34,2.1)
computing_roots(7/1,-6/7,1/2)
