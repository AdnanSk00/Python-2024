'''

For n = 3
    *
  * * * 
* * * * *

'''

n = int(input("Enter no of rows: "))

for i in range(1, n+1):
  print("  " * (n-i), end="")
  print(" *" * (2*i-1), end="")
  print("")

