def isHappy(n: int) -> bool:
    # Floyd's Cycle-Finding Algorithm
    # O(log(n)) time | O(1) space
    def get_next(number: int) -> int:
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit**2
            number //= 10
        return total_sum

    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1
