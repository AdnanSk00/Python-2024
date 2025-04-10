'''
n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("* " * (n - i + 1))

'''

def pattern(n):
    if(n == 0):
        return      # return - function will stop(Baat khatm, ab jao)
    print("* " * n)
    pattern(n-1)

n = int(input("Enter a number: "))
pattern(n)