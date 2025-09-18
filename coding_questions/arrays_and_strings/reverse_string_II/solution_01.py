def reverseStr(s: str, k: int) -> str:
    # two pointer approach
    # O(n) time, O(n) space
    s = list(s)
    for i in range(0, len(s), 2 * k):
        left = i
        right = min(i + k - 1, len(s) - 1)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)
