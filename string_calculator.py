import re

def add(numbers):

    if not numbers:
        return 0

    # default delimiters
    delimiter = r'[,\n]'

    # check for custom delimiters in string
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delimiters = parts[0][2:]
        delimiter = re.escape(custom_delimiters)
        numbers = parts[1]

    nums = re.split(delimiter, numbers)
    int_nums = [int(num) for num in nums]
    negatives = [num for num in int_nums if num < 0]

    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    return sum(int_nums)