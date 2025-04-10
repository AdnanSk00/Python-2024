
def rem(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n



list = ["Zoaib", "Shifan", "Guddu", "Faizan", "an", "Adnan","fun"]

print(rem(list, "an"))

