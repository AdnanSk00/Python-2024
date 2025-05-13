# lambda arguments: expressions
# can be used as a normal function

# def square(n):
#     return n*n

square = lambda x: x*x
print(square(6))

sum = lambda a,b,c: a+b+c
print(sum(4, 2, 6))