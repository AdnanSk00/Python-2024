marks = {
    "Rehan" : 99,
    "Nabil" : 92,
    "Abuzar" : 93,
    0 : "Fahad"
}

# print(marks);

# print(len(marks));
# print(marks.items());
# print(marks.keys());
# print(marks.values());
# marks.update({"Rehan": 91, "Aman": 89})
print(marks);

print(marks.get("Rehan"));
print(marks["Rehan"]);
print(marks.get('Abuzar', '93'))

# print(marks.get("Rehan2"));   # Prints None
# print(marks["Rehan2"]);       # Returns an error

# ----------------------------------------------

# marks.clear()
# print(marks);
# print(marks.clear());

# new_marks = marks.copy()
# print(new_marks);

keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict);

# marks.pop('Rehan', '99')
# print(marks.popitem())
# print(marks);




