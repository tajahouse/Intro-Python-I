x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
txt = '{x}, {y}, {z}'
print(txt.format(x=x, y=y, z=z))
# Use the 'format' string method to print the same thing
print(f'{x}, {y}, {z}')
# Finally, print the same thing using an f-string