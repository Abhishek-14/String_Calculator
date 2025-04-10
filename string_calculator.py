import re

def add(numbers):

    if not numbers:
        return 0

    nums = re.split(r'[,\n]', numbers)
    return sum(int(num) for num in nums)