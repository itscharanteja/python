def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

string = input("Enter a string: ")
char_count = count_chars(string)
print("Character count:", char_count)
