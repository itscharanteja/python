def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    letter_count = 0
    
    for char in word:
        if char.isalpha():
            letter_count += 1
            if char in vowels:
                vowel_count += 1
    
    return letter_count, vowel_count, (vowel_count / letter_count) * 100

# Get input from the user
word = input("Enter a word: ")

# Calculate counts and percentage
letter_count, vowel_count, vowel_percentage = count_vowels(word)

# Display the results
print(f"Number of letters in the word: {letter_count}")
print(f"Number of vowels in the word: {vowel_count}")
print(f"Percentage of vowels in the word: {vowel_percentage:.2f}%")
