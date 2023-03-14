# Create a Tuple ( Unchangeable Elements)
names = ("Baha", "Ali", "Abdalh")
print(f"{type(names)}    {names}")
# Convert Tuple to List ( to change tuple element) 
x = list(names)
x[1] = "Sara"
names = tuple(x)
print(f"{type(names)}    {names}")