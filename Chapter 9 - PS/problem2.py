import random

def game():
    print("Your are playing the game..")
    score = random.randint(1, 62)

    # Fetch the hiScore
    with open("hiScore.txt") as f:
        hiScore = f.read()
        if(hiScore!=""):
            hiScore = int(hiScore)
        else:
            hiScore = 0

    print(f"Your score: {score}")
    if(score > hiScore):
        # write this hiScore to the file
        with open("hiScore.txt", "w") as f:
            f.write(str(score))

    return score

game();