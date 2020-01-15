import collections
import math
import random

def entropy(data):
    e = 0
    counter = collections.Counter(data)
    l = len(data)
    for count in counter.values():
        # count is always > 0
        p_x = count / l
        e += - p_x * math.log2(p_x)

    return e


def Average(data):
    sum=0.0
    l=len(data)
    
    for i in data:
        sum+=i

    return sum/l


def S(data):
    s=0.0
    Numerator =0.0
    denominator=len(data)
    
    for value in data:
        Numerator+=math.pow((value-Average(data)),2)

    s=math.sqrt(Numerator/denominator)

    return s






def main():
    arr_x=[4,9,11,12,17,5,8,12,14]

    print("The  standard_deviation  is : {}".format(S(arr_x)))


if __name__ == '__main__':
    main()
