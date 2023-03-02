# Ask user to write a Number
n = input("Give Me A Number: ")

# input function is ( str ) we need to conver it to ( int )
number = int(n)

# chick the number if it is ==> Positive / Negative / Zero
if number > 0:
     print(f"The Number {number} is Positive.")
elif number < 0:
     print(f"The Number {number} is Negative.")
else:
     print(f"The Number {number} is Zero.")