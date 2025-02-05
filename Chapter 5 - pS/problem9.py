# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9

# List can not be included as an element in set
# Value can not be changed by indexing in set
# Because sets in python require all their elements to be immutable and hashable. Lists are mutable and not hashable. So they cannot be added to a set.