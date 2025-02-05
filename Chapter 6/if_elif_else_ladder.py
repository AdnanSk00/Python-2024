a = int(input("Enter your age: "))

# if elif else ladder

if(a>=18):
    print("You are above the age of consent");
    print("I am also in if block");

elif(a<0):
    print("You entered invalid negative age");
    
elif(a==0):
    print("Your entered zero which is not a valid age");
    
else:
    print("Your are below the age of consent");


print("End of program");





# Note: The tab space after if/elif/else: or before print() is called 'indent'.It means if/elif/else consist that indent code in their block.