# name in pascal case
# this program will ask the user to enter full name in incorrect casing and print it in pascal case

# ask the user to enter full name in incorrect casing
fullname = input("Enter your full name in incorrect casing: ")

# convert the to pascal case
pascal_case = fullname.title().split() # convert the full name to title case and split it into a list

# print the name in pascal case
print(''.join(pascal_case)) # join the list of names into a string and print it