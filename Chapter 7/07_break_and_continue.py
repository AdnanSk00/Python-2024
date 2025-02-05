## The Break Statement :-
for i in range(36):
    if(i == 9):
        print("\n");
        break       # Exit the loop right now!
    print(i)
    


## The Continue Statement :-
for i in range(36):
    print("Printing");
    if(i == 9):
        continue       # Skip this iteration right now!
    print(i)