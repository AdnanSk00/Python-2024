with open("log.txt", "r") as f:
    lorem34 = f.read()

if("python" in lorem34):
    print("Yes python is present")
else:
    print("No, python is not present")