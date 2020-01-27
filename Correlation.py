import math


def Average(data):
    sum=0.0
    l=len(data)

    for i in data:
        sum+=i

    return sum/l


def S(data):               #standard deviation
    s=0.0
    Numerator =0.0
    denominator=len(data)


    for value in data:
        Numerator+=math.pow((value-Average(data)),2)

    s=math.sqrt(Numerator/denominator)

    return s


def correlation(A,B):
    Numerator = 0.0
    Denominator = 0.0
    l=0
    if len(A)<len(B):l=len(B)
    else:l=len(A)
    ave_A=Average(A)
    ave_B=Average(B)
    for i in range(l):
        Numerator+=(A[i]-ave_A)*(B[i]-ave_B)

    Denominator=((S(A)*S(B))*l)

    return Numerator/Denominator
