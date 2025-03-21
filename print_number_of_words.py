# print number of words
# this program will ask the user to enter a statemtent and then it will count the number of words

# ask the user to enter a statement
statement = input("Enter a statement: ")

# split the statement into words and count the number of words
number_of_words = len(statement.split())

# print the number of words in the statement
print(number_of_words) 