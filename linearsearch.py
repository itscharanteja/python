def search_and_count(x,arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count+=1
    return count

print(search_and_count(2,[2,2,2,2,2]))
print(search_and_count(2,[2,2,2,2,2]))
print(search_and_count(2,[2,2,2,2,2]))