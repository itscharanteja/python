def bubble_sort(numbers: List[int]) -> List[int]:
    """

    @rtype: object
    """
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
bubble_sort([5, 2, 7, 1, 3])
