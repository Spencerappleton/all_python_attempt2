temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
else:
    print("It is not hot outside")
print("Done")

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")
print("Done")


if temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")



user_name = input("What is your name? ")
if user_name == "Paul" or user_name == "Mary":
    print("You have a nice name.")
else:
    print("Your name is ok.")
    
user_name = input("What is your name? ")
if user_name.lower() == "paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")
    
user_name = input("What is your name? ")
# print (user_name.lower()