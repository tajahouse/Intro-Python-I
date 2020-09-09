x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("From the string modulo operator...\n x is %.2d, y is %f, z is %s" % (x,y,z))
txt = '{x}, {y}, {z}'
print("From format string \n", txt.format(x=x, y=y, z=z))
# Use the 'format' string method to print the same thing
print("The best way to do this \n",f'{x}, {y}, {z}')
# Finally, print the same thing using an f-string