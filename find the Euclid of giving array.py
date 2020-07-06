import  random
import math

def Euclid(data):
    Center1=random.randint(0,len(data)-1)
    reuslt=0

    for value in data:
        reuslt+=math.sqrt(math.pow(value,2)+math.pow(data[Center1],2))

    return reuslt


def main():
    arr=[2,4,6,8,16]
    print("The Firts Euclid of {} ".format(Euclid(arr)))


if __name__ == '__main__':
    main()
