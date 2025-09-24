def isHappy(n: int) -> bool:
    """
    The logic is to keep track of every number seen during the process.
    If you see a number for a second time, it means you're in a cycle,
    and the number is not happy.

    Algorithm: Hash Set Cycle Detection
    Time Complexity: O(log n)
    Space Complexity: O(log n) - for the hash set
    """

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        currentSum = 0
        while n > 0:
            digit = n % 10
            currentSum += digit * digit
            n //= 10
        n = currentSum
    return n == 1
