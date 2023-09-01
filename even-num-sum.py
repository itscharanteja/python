def compute_even_sum(n):
    even_sum = 0
    
    for i in range(1, n+1):
        if i % 2 != 0:  # If the number is odd
            continue
        even_sum += i
    
    return even_sum

# Get input from the user
try:
    n = int(input("Enter a natural number: "))
    if n < 1:
        print("Please enter a valid natural number.")
    else:
        result = compute_even_sum(n)
        print(f"The sum of even numbers within the range 1 to {n} is: {result}")
except ValueError:
    print("Please enter a valid natural number.")
