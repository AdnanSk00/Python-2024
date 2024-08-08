# We can't change existing string therefor we use list. See below Eg
# a = "adnan"
# a[0] = "A"
# print(a[0]);   # show error
   

friends = ["Apple", "Orange", 2, 786.03, False, "Askalan", "Shaam"]

print(friends[0]);

friends[0] = "Grapes" 
# Unlike Strings Lists are mutable
print(friends[0]);
print(friends[5]);
print(friends[1:4]);
print(friends[1:7:2]);

