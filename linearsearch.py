def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
a = [1,2,34,5,6,7,3,4,2,8,9,5,55,65,453,343]
s = search(a,242)

if s == -1:
    print("No value present in the list")
else:
    print(s)