# Just empty Speace from up
print()

# (( Mutable )) means that once a sequence has been defined,
# we can change individual elements of that sequence,
# and (( Ordered )) means that the order of the objects matters.

# 1-    Strings:
#           Ordered: Yes
#           Mutable: No
String = "Baha"
print(f'This is Srting ==> {String}')
print(f"Access to String ==> {String[0], String[1], String[2], String[3]}")
print(f'This Srting ==> {String} Unchangeable ( Unmutable ).\n\n')

#   Lists:
#       Ordered: Yes
#       Mutable: Yes
Lists = []
print(f"Empity List ==>  {Lists}")
Lists.append("Baha")
Lists.append("Ali")
Lists.append("Adam")
print(f"{Lists}\n")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in thislist:
    Lists.append(i)
print(Lists)
print(f"Access List Items (Lists[3:7]) ==> {Lists[3:7]}\n")
print(Lists)
Lists[3] = "Anna"
print(f"Change List Items by INDEX ==>{Lists}\n")
print(Lists)
Lists[4:7] = ["Noor", "Ashe", "Lux"]
print(f"Change Multiple List Items by INDEX ==>{Lists}\n")
print(Lists)
# Insert Item in List in Specefic INDEX
# which mean:
# mango become ([mango] + 1)
# Orange INSERT in ([mango])
Lists.insert((len(Lists) - 1), "Orange")
print(f" Insert Item in List in Specefic INDEX ==> {Lists}")
print(Lists)
Lists.remove("Orange")
print(f"Remove List Item by secific value ==> {Lists}\n")
print(Lists)
Lists.pop(5)
print(f"Pop out List Item by secific INDEX ==> {Lists}\n")
print(Lists)
del Lists[3]
print(f"Delete List Item by secific INDEX (del Lists[3]) ==> {Lists}\n")
print("Loop over the List")
for i in range(len(Lists)):
    print(f"Item: {i} Value: {Lists[i]}")
print()

print(Lists)
print(Lists)
Lists.clear()
print(f"Delete All List Items  ==> {Lists}\n")




# Just empty Speace from down
print()