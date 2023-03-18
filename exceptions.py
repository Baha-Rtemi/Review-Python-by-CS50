import sys

try:
    x = int(input("give me a first  number: ".title()))
    y = int(input("give me a second number: ".title()))
except ValueError:
    print("you can't give me a letter just a number.".title())
    sys.exit(1)

try:
    z = x / y 
except ZeroDivisionError:
    print("you can't davide by 0.".title())
    # EXIT THE PROGRAME ( FALSE)
    sys.exit(1)


print(f"""
      {"the first number is: ".upper()}    {x}
      {"the second number is: ".upper()}   {y}
      {"the result is: ".upper()}          {z}
      """)