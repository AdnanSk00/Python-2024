list = [56, "Adnan", False, "Him", "Awais", "Raiyyan", "Saim", "Sahil"]


i = 0
# while(i<len(list)):
    # print(list[i])
    # i += 1
    
# -------------------------------------

while(i<len(list)):
    if(i==0):
        print(f"[{list[i]}",end=", ")
    elif(i==len(list)-1):
        print(f"{list[i]}]")
    else:
        print(list[i],end=", ")
    i += 1
