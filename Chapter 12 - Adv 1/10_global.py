a = 56      # local variable

def fun():
    # global a
    a = 18
    print(a)

fun()
print(a)