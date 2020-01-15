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



def main():
    arr_x=[]
    arr_y=[]
    rnd=random
    n=40  #lenght of Arrays
    for i in range(0,n):
        n= int(rnd.randint(1,6))
        arr_x.append(n)
        n=int(rnd.randint(1,6))
        arr_y.append(n)

    x_entropi=entropy(arr_x)
    y_entropi=entropy(arr_y)
    x_entropi=x_entropi/math.log2(n)
    y_entropi = x_entropi / math.log2(n)
    print("The Entropi of X  is : {} and The Entropi of Y is : {}".format(x_entropi,y_entropi))


if __name__ == '__main__':
    main()
