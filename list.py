num = [22,77,44,65,89,34,38,34]

max = num[0]

for n in num:
    if n > max:
        max = n
print(max)
#remove duplicates
unique = []

for i in num:
    if i not in unique:
        unique.append(i)
        
print(unique)

