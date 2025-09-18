def reverseStr(s: str, k: int) -> str:
    # slicing approach
    # O(n) time, O(n) space
    s_arr = list(s)
    for i in range(0, len(s_arr), 2 * k):
        s_chunk = s_arr[i : i + k]
        s_arr[i : i + k] = s_chunk[::-1]
    return "".join(s_arr)
