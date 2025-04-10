def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 3
b = 10
c = 8

print(f"{greatest(a, b, c)} is greatest")
