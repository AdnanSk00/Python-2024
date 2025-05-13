import random
randNum = random.randint(1, 100)

userNum = -1
guesses = 1
while(userNum != randNum):
    userNum = int(input("Guess the number: "))
    if(userNum > randNum):
        print("Lower number please")
        guesses += 1
    elif(userNum < randNum):
        print("Higher number please")
        guesses += 1

print(f"You haave guessed the number {randNum} correctly in {guesses} attempt")