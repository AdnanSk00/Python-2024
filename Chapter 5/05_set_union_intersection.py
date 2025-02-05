s1 = {11, 33, 44, 22}
s2 = {55, 22, 33}

print(s1.union(s2));
print(s1.intersection(s2),"\n");

print(s1 - s2);
print({22, 33}.issubset(s1));
print({33}.issubset(s2));
print(s1.issuperset({22, 33}));



