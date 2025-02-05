Marks = int(input("Enter your Marks: "))

if(Marks<=100 and Marks>=90):
    grade = "Ex"

elif(Marks<90 and Marks>=80):
    grade = "A"

elif(Marks<80 and Marks>=70):
    grade = "B"

elif(Marks<70 and Marks>=60):
    grade = "C"

elif(Marks<60 and Marks>=50):
    grade = "D"

else:
    grade = "F"

print("Your grade is:",grade);
