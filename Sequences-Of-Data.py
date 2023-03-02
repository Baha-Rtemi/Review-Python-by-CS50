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
print(f'This Srting ==> {String} Unchangeable ( Unmutable ).')

#   Lists:
#       Ordered: Yes
#       Mutable: Yes
Lists = []
print(f"Empity List ==>  {Lists}")
Lists.append("Baha")
Lists.append("Ali")
Lists.append("Adam")
print(Lists)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in thislist:
    Lists.append(i)
print(Lists)





# Just empty Speace from down
print()