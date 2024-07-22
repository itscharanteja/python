def num_count(n):
    count = 0

    while n>0:
        count += 1

        n = n//10

    return count

print(num_count(5221211213))