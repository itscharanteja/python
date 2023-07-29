import re


def extract_emails_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return ';'.join(re.findall(r'\S+@\S+', file.read()))
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."


if __name__ == "__main__":
    file_path = "mails.txt"  # Replace this with the actual path to your file
    result = extract_emails_from_file(file_path)
    print(result)
