"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# file = open("foo.txt", "w")
''' Something to remember. So I didn't write the correct command. What I did was actually create a foo.txt. Since foo.txt already existed, the command above actually overwrote the already existing file... I don't know how to retrieve it, so I will have to copy and paste what was previously in there... if I just want to print what is in there, the code below should work.'''

with open('foo.txt') as foo_file:
    read_data = foo_file.read()

    print(read_data)

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file = open("bar.txt", "w")
file.write("Some content that I want to write\n")
file.write("...will be in this file.\n")
file.write("And I will commit this to memory!\n")
file.close()