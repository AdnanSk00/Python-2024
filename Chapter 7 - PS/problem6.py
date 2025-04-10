# 5! = 5 X 4 X 3 X 2 X 1

n = int(input("Enter a number: "))

fac = 1;
for i in range(1, n+1):
    fac *= i
    # print(f"{fac} ",end="");
    
print(f"Factorial of {n} = {fac}");
    
        

# i = 1;
# fac = 1;
# while(i<=n):
#     fac *= i
#     i += 1

# print(fac);