import re

def insert_multiplication(expression):
    # Insert multiplication symbol after a number followed by a letter
    expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
    
    # Insert multiplication symbol before a number enclosed in parentheses
    expression = re.sub(r'(\))(\d)', r'\1*\2', expression)
    
    return expression

user_input = input("Enter an algebraic expression: ")

result = insert_multiplication(user_input)

# Print the result
print("Result:", result)
