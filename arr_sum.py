def hourglassSum(arr):
    # Write your code here
    max_sum = -63
    
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            
            middle = arr[i+1][j+1]
            
            last = sum(arr[i+2][j:j+3])
            
            hourglass = top + middle + last
            
            if hourglass > max_sum:
                max_sum = hourglass
    return max_sum
            
            
print(hourglassSum([[1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]]))