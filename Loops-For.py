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
print("#"*10, end="\n\n")
print("RANGE()")
print("#"*10, end="\n\n")
print("without range():")
for i in [0,1,2,3,4,5,6]:
  print(i)
print("#"*10, end="\n\n")
print("with range():")
for i in range(7):
  print(i)
print("#"*10, end="\n\n")
print("printout numbers from 5 to 8 :")
for i in range(5,9):
  print(i)
print("#"*10, end="\n\n")
print("printout numbers from 10 to 100 and the ingerment is 10 :")
for i in range(10,110,10):
  print(i)