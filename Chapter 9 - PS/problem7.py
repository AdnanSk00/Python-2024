
with open("log.txt", "r") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineNo}")
        break
    lineNo +=1

else:
    print("No, python is not present")