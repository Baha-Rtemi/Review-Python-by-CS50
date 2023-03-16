# Full_Name = ["Baha","Apoled","Ali","Rtemi"]
# for name in Full_Name:
# 	print(name)
# print("#################")
# for charecters in Full_Name[0]:
# 	print(charecters)
# print("#################")
# for x in Full_Name:
# 	if x == "Apoled":
#       break
# 	  print(x)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break
###############################################
name = "Baha"
for char in name:
  print(char)
print("#"*10, end="\n\n")
names = ["Baha","Ali","Abdalh","Apoled"]
for name in names:
  # printout all names
  print(name)
print("#"*10, end="\n\n")
# printout names without what's after "Ali" name
for SpecialName in names:
  print(SpecialName)
  if SpecialName == "Ali":
    break
print("#"*10, end="\n\n")
# printout names without "Ali" name and what's after it
for SpecialNAME in names:
  if SpecialNAME == "Ali":
    break
  print(SpecialNAME)
print("#"*10, end="\n\n")
# printout all names without "Ali" name
for name in names:
  if name == "Ali":
    continue
  print(name)
