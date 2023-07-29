def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
                if arr[j]>arr[j+1]:
                    
                    arr[j],arr[j+1]= arr[j+1],arr[j]
            
arr = list(input("Enter elements "))
b = arr

sort(arr)
print(arr," ")
print(b," ")

