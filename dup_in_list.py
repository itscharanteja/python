def dups(lst):
    unique = []
    for i in lst:
        if lst.count(i) == 1 and i not in unique:
            unique.append(i)
    return unique

# Take user input as comma-separated values
user_input = input("Enter a list of comma-separated values: ")

# Convert the string input to a list of integers
lst = [int(i) for i in user_input.split(',')]

# Find unique in the list
uniq = dups(lst)

# Print the list of unique
print("The unique in the list are: ", uniq)
