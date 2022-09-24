def buble(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
            if swapped == False:
                break    
arr=[1,6,4,3,9,4,7,3,8,5]

buble(arr)

print("Sorted array is:",arr)
