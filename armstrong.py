def armstrong(n):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp%10
        temp = temp // 10
        sum += digit ** len(str(n))
    return sum==n

print(armstrong(153))