def classify_file(file_path):
    file_extension = file_path.split('.')[-1].lower()

    python_extensions = ['py']
    c_extensions = ['c', 'cpp', 'h']
    txt_extension = ['txt']

    if file_extension in python_extensions:
        return "Python Program"
    elif file_extension in c_extensions:
        return "C Program"
    elif file_extension in txt_extension:
        return "Text File"
    else:
        return "Some other file"


file_path = input("Enter the path to the file: ")
classification = classify_file(file_path)
print(f"The given file is classified as: {classification}")
