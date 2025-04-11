a = int(input("Enter your age: "))

# if statement no: 1
if(a%2 == 0):
    print(a,"is even in if statement 1");

# End of if statement no: 1


# if statement no: 2
if(a>=18):
    print("You are above the age of consent");
    print("I am also in if block");

elif(a<0):
    print("You entered invalid negative age");
    
elif(a==0):
    print("Your entered zero which is not a valid age");
    
else:
    print("Your are below the age of consent");

# End of if statement no: 2


print("End of program");




