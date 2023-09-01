def capitalize_file_content(filename):
    try:
        # Read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Capitalize the content
        capitalized_content = content.upper()
        
        # Write the capitalized content back to the file
        with open(filename, 'w') as file:
            file.write(capitalized_content)
        
        print(f"File '{filename}' has been capitalized.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Get input from the user
file_name = input("Enter the name of the text file: ")

# Call the function to capitalize the file's content
capitalize_file_content(file_name)
