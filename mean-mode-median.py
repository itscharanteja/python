import statistics

# Take input from the user
num_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert input to integers
num_list = [int(num) for num in num_list]

# Calculate the mean, median, and mode
mean = statistics.mean(num_list)
median = statistics.median(num_list)
mode = statistics.mode(num_list)

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
