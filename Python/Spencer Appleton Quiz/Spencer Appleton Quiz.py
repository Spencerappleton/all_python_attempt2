y = 0

print ("It's time for a quiz")
print ("Let's begin")
one = input("1. How many star wars movies have there been: ")
if one == "7":
    print ("correct")
    y = y + 1
else:
    print ("incorrect")
    
winner = input("2. Who won World War Two, The Axis or Allies: ")
if winner == "Allies" or winner == "allies":
    print ("correct")
    y = y + 1
else:
    print ("incorrect")


x = input("3. 23+16 = ")
if x == "39":
    print ("correct")
    y = y + 1
else:
    print ("incorrect")


print ("4. How many planets are in the Sol system, ")
print ("A = 10")
print ("B = 9")
print ("C = 14")
print ("D = 8")
planets = input("The answer is: ")
if planets == "B" or planets == "b":
    print ("correct")
    y = y + 1
else:
    print ("incorrect")

element = input("5. What is the smallest element on the Periodic Table:")
if element == "Hydrogen" or element == "hydrogen":
    print ("correct")
    y = y + 1
else:
    print ("incorrect")

print ("you got:")
print (y)
print ("out of 5")