#Question 1

import math

def My_fUNC(X1=float,X2=float,X3=float):
    if type(X1)==float and type(X2)==float and type(X3)==float:
        if (X1+X2+X3)!=0:
            sol=((X1+X2+X3)*(X2+X3)*X3)/((X1+X2+X3))
            return sol
        else:
            print("Not a number – denominator equals zero")
    else:
        print("Error: parameters should be float")


#question 2:
def convert(hours,minutes):
    if type(hours)== float or type(hours)== int and type(minutes)== int or type(minutes)== float:
        if hours>0 and minutes>0:
            hours_split=math.modf(hours)
            minutes_convert=hours_split[0]*60*60
            hours_convert=hours_split[1]*60*60
            minutes_convert_2 = minutes*60
            print(minutes_convert + minutes_convert_2 + hours_convert)
        else:
            print("input error")
    else:
        print("input error")































