# Open the file in read mode using 'with', which automatically closes the file

f = open("file.txt")  
print(f.read())
f.close()


# The same can be writter using 'with' statement like this:

with open("file.txt") as f:
    print(f.read())   

# You dont have to explicitly close the file

# -----------------------------------------

# We can now use multiple context managers in a single with statement more cleanly written in Advanced Python 1
# using the parenthesised context manager

# with (
# open('file1.txt') as f1,
# open('file2.txt') as f2
# ):
# Process files