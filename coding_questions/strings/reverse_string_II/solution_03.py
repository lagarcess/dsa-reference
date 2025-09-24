def reverseStr(s: str, k: int) -> str:
    # Using extra space (less efficient)
    # O(n) space, O(n) time
    s_list = list(s)
    for i in range(0, len(s_list), 2 * k):
        s_list[i : i + k] = reversed(s_list[i : i + k])
    return "".join(s_list)
