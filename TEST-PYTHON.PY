# printout numbers from 1 to 10 but without number 5
print("#"*10, end="\n\n")
print("printout numbers from 1 to 10 but without number 5")
i = 0
while i < 20:
    i += 1
    if i == 5:
        continue
    print(i)
    if i == 10:
        break
print("#"*10, end="\n\n")
print("printout a message when the loop is over")
i = 0
while i < 6:
    print(i)
    i += 1
else:
    print(f"The number i (({i})) is no longer less than number SIX")