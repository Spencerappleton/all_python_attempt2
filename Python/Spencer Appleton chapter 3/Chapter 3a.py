# Variables used in the example if statements
a = 4
b = 5
 
# Basic comparisons
if a < b:
    print("a is less than b")
 
if a > b:
    print("a is greater than b")
 
print("Done")


if a <= b:
    print("a is less than or equal to b")
 
if a >= b:
    print("a is greater than or equal to b")
    
    
a = 9
b = 9

# Equal
if a == b:
    print("a is equal to b")
     
# Not equal
if a != b:
    print("a and b are not equal")    
    


if a == 1:
    print("If a is one, this will print.")
    print("So will this.")
    print("And this.")
     
print("This will always print because it is not indented.")    




a = 2
b = 3
c = 1



# And
if a < b and a < c:
    print("a is less than b and c")
 
# Non-exclusive or
if a < b or a < c:
    print("a is less than either b or c (or both)")
    
    
    



# Boolean data type. This is legal!
a = True
if a:
    print("a is true")    
    
    
# How to use the not function
if not(a):
    print("a is false")




a = 3
b = 3
# This next line is strange-looking, but legal.
# c will be true or false, depending if
# a and b are equal.
c = a == b
# Prints value of c, in this case True
print(c)