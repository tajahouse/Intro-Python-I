# Write a function is_even that will return true if the passed-in number is even.


# YOUR CODE HERE

# Read a number from the keyboard

def is_even(num):
    if num % 2 == 0:
        return "EVEN!"
    else:
        return "odd"
num = input("Enter a number: ")
num = int(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
print(is_even(num))
# YOUR CODE HERE

