# name in snake case
# this program will convert the user's inputted full name in snake case

# ask for the user's full name in incorrect casing
fullname = input("Enter your full name in incorrect casing: ")

# convert to snake case 
snake_case = fullname.lower() # convert the full name to lowercase

# print the snake case name
print(snake_case.replace(' ', '_')) # replace the spaces with underscores and print the name in snake case