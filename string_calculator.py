
def add(numbers):

    if not numbers:
        return 0

    nums = numbers.split(",")
    return sum(int(num) for num in nums)