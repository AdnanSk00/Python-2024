# Using walrus operator :=

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)

if (p := 10) < (q := 9):
    print(f"{p} is less than {q}")
else:
    print(f"{p} is greater than {q}")