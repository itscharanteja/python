def test_even_numbers():
    # Test Case 1: List of all even numbers
    input_list = [2, 4, 6, 8, 10]
    expected_output = True
    assert even_numbers(input_list) == expected_output, "Test Case 1 failed"

    # Test Case 2: List with odd numbers
    input_list = [1, 3, 5, 7, 9]
    expected_output = False
    assert even_numbers(input_list) == expected_output, "Test Case 2 failed"

    # Test Case 3: Empty list
    input_list = []
    expected_output = True  # An empty list has no odd numbers
    assert even_numbers(input_list) == expected_output, "Test Case 3 failed"

    # Test Case 4: List with a mixture of even and odd numbers
    input_list = [2, 5, 8, 10, 13]
    expected_output = False
    assert even_numbers(input_list) == expected_output, "Test Case 4 failed"

    # Test Case 5: List with negative even numbers
    input_list = [-4, -6, -8, -10, -12]
    expected_output = True
    assert even_numbers(input_list) == expected_output, "Test Case 5 failed"

    print("All test cases passed!")

# Even numbers function


def even_numbers(input_list):
    for num in input_list:
        if num % 2 != 0:
            return False
    return True


# Run test cases
test_even_numbers()
