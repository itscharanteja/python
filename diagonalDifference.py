def d(arr):
    # Write your code here
    rs = 0
    for i in range(len(arr)):
        rs+=arr[i][i] - arr[i][len(arr) - i - 1]
    return abs(rs)

ar = [[1,2,3], [2,3,5], [2,5,7]]
print(d(ar))