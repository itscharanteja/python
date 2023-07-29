f = input("Enter name of the file: ")
with open(f, "r") as file:
    data = file.read()
cont = data.split()
uniq = list(set(cont))

uniq.sort()
print("Unique words in alphabetical order:")
for word in uniq:
    print(word)

print(list(set(cont)))
