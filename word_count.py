# initialize an empty dictionary
word_count = {}

# read the text from the file
text = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car. Studying python is very important. perfect Plan B makes us perfect in python and Machine Learning"

# split the text into words
words = text.split()

# count the number of occurrences of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# print the word counts
output = " "
for word, count in word_count.items():
    output += f"{word} {count} "

# find the word with the largest count
most_common_word = max(word_count, key=word_count.get)

# print the result
output += f"\nDone the {word_count['the']}"
print(output)


print(word_count)