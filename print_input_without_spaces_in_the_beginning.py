# print input without spaces in the beginning
# this program will print the inputted name without any spaces in the beginning

# ask for the users full name with several spaces in the beginning
fullname = input("Enter your full name with several spaces in the beginning: ")

# remove leading spaces and print the name
print(fullname.lstrip())    # print the name without any leading spaces


