# Function to add a birthday to the dictionary
def add_birthday(birthday_dict, name, date):
    birthday_dict[name] = date

# Function to search for a birthday in the dictionary
def search_birthday(birthday_dict, name):
    if name in birthday_dict:
        return birthday_dict[name]
    else:
        return None

# Main program
def main():
    # Create an empty dictionary to store birthdays
    birthday_dict = {}

    # Take input from the user for birthdays in the format "name:dd-mm-yyyy separated by commas"
    data = input("Enter birthdays (name:dd-mm-yyyy separated by commas): ")

    # Split the input string into a list of strings using comma as a delimiter
    birthdays = data.split(",")

    # Loop through each string in the birthdays list and extract the name and date
    for birthday in birthdays:
        name, date = birthday.split(":")
        add_birthday(birthday_dict, name.strip(), date.strip())

    # Print the dictionary
    print(birthday_dict)

    # Take input from the user for a name to search in the dictionary
    name = input("Enter a name to search: ")

    # Search for the birthday in the dictionary
    birthday = search_birthday(birthday_dict, name)

    # Output the result
    if birthday:
        print("The birthday of", name, "is", birthday)
    else:
        print("No data found for", name)

# Run the main program
if __name__ == "__main__":
    main()
