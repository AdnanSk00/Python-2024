from functools import reduce

l = [1, 4, 23, 53, 0, 89, 56, 23]

def greater(m, n):
    if(m>n):
        return m
    return n

print(reduce(greater, l))