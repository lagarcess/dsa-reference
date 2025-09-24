def isHappy(n: int) -> bool:
    # Hash Set Cycle Detection with Pythonic Sum and Generator Expression
    # O(log(n)) time | O(log(n)) space
    seen = set()
    cur = n
    while cur not in seen:
        seen.add(cur)
        cur = sum(int(digit) ** 2 for digit in str(cur))
    return cur == 1
