def find_insert_position(sorlist, newelmt):
    for i in range(len(sorlist)):
        if sorlist[i] >= newelmt:
            return i 
    
    return len(sorlist)

spk = [10, 20, 30, 40, 50]
val = int(input("write 1 val: "))

pos = find_insert_position(spk, val)

print("sort spisok:", spk)
print("new el:", val)
print("pos (indx):", pos)

spk.insert(pos, val)
print("spisok after ins:", spk)