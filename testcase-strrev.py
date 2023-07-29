def test_reverse_string():
    # Test Case 1: Single-word string
    input_str = "Hello"
    expected_output = "olleH"
    assert reverse_string(input_str) == expected_output, "Test Case 1 failed"

    # Test Case 2: Empty string
    input_str = ""
    expected_output = ""
    assert reverse_string(input_str) == expected_output, "Test Case 2 failed"

    # Test Case 3: String with special characters
    input_str = "!@#$%^&*()"
    expected_output = ")(*&^%$#@!"
    assert reverse_string(input_str) == expected_output, "Test Case 3 failed"

    # Test Case 4: String with spaces
    input_str = "Hello World"
    expected_output = "dlroW olleH"
    assert reverse_string(input_str) == expected_output, "Test Case 4 failed"

    # Test Case 5: String with numbers
    input_str = "12345"
    expected_output = "54321"
    assert reverse_string(input_str) == expected_output, "Test Case 5 failed"

    print("All test cases passed!")

# Reverse string function


def reverse_string(input_str):
    return input_str[::-1]


# Run test cases
test_reverse_string()
