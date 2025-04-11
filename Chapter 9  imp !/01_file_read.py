# RAM :- Volatile(temperory memory)
        # Fast execution of program
# HDD :- Non Volatile(Hard disk, SSD, PenDrive)

# FILE :- File is used to stored data in data storage
        # Can read and write from file

'''
a = "a very long string with emails"
emais = []
3 seconds
'''


# open("filename", "mode of opening(read mode by default)")
# open("file.txt", "r/w")

f = open("file.txt")    # Open file in read mode

data = f.read()         # Read its contents

print(data)             # Print its contents

f.close()               # Close the file

