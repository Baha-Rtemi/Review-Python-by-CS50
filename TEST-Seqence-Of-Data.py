set = set()

set.add(1)
set.add("Baha")
set.add("A")
set.add(True)
print(set)
set.remove("Baha")
print(set)
# You cannot access items in a set by referring to an index or a key.
# print(set[0])