def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 34234, 65, 53341, 56, 735, 920, 55]

f = list(filter(divisible5, a))
print(f)
