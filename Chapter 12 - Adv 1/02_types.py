n : int = 5

name : str = "Adnan"

def sum(a: int, b: int) -> int:
    return a + b

Jama = sum(3, 5)
print(Jama)


# Variable type hint
age: int = 25

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Usage
print(greeting("Alice")) # Output: Hello, Alice!