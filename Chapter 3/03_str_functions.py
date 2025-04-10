'''
1  - len()
2  - startsWith()
3  - endsWith()
4  - capitalize()
5  - title()
6  - lower()
7  - upper()
8  - count()
9  - find()
10 - join()
11 - split()
12 - replace()
13 - strip()
14 - lsstrip()
15 - rstrip()
16 - isalpha()
17 - isdigit()
18 - islower()
19 - isupper()
20 - swapcase()
21 - format()
22 - center()
23 - zfill()

All these are Case Sensitive(h != H)
'''

name = "    adnanShAIkh saLim   "

print(name, len(name));
print(name.endswith("Im"));
print(name.startswith("ad"));
print(name.capitalize());   # Capitalize the first character of the string 
print(name.title())     # Capitalize the first character of each word in a string
print(name.lower());
print(name.upper());
print(name.count("n"));
print(name.find("h"));
print(name.replace("a", "A"));
print(name.strip());    # Removes leading and trailing whitespace
print(name.lstrip());    # Removes leading whitespace
print(name.rstrip());    # Removes trailing whitespace
print(name.zfill(30));
print(name.center(25))    
