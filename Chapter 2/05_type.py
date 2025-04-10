a = 31
j = type(a)     # class <int> 

print(j);

# o = "Bhai"
o = 7.022
t = type(o)     # class <float>

print(t);


m = "313.4"
print(m, type(m))
n = float(m)         # but the type should be float
print(n)

w = type(m)
print(w);

u = type(n)
print(u);


name = "Hinata";
print(name, type(name))

# toFloat = float(name)     # Error can't do this
# toFloat = int(name)
# print(toFloat)