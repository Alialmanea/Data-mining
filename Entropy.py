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
    rnd=random
    n=100
    for i in range(0,n):
        n= int(rnd.randint(1,6))
        arr_x.append(n)

    x_entropi=entropy(arr_x)

    print("The Entropi   is : {}".format(x_entropi))


if __name__ == '__main__':
    main()
