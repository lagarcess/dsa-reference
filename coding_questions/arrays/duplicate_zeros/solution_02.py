from typing import List


def duplicateZeros(arr: List[int]) -> List[int]:
    n = len(arr)
    possible_dups = 0
    last_kept_idx = -1
    # Pass 1: Find how many zeros can be duplicated and the last element to be kept.
    for i in range(n):
        # If we are at the boundary where adding this element (and its potential
        # duplicate if it's a zero) would fill the array, this is the last element.
        if i + possible_dups >= n - 1:
            last_kept_idx = i
            break

        if arr[i] == 0:
            possible_dups += 1

    # Pass 2: Iterate backwards from the last kept element and write to the end.
    write_pointer = n - 1
    read_pointer = last_kept_idx

    # Special case: If the last kept element was a zero that gets cut off,
    # we only write it once without duplicating.
    if read_pointer == n - 1 - possible_dups and arr[read_pointer] == 0:
        arr[write_pointer] = 0
        write_pointer -= 1
        read_pointer -= 1

    while read_pointer >= 0:
        if arr[read_pointer] == 0:
            # Duplicate the zero
            arr[write_pointer] = 0
            write_pointer -= 1
            arr[write_pointer] = 0
        else:
            # Copy the non-zero element
            arr[write_pointer] = arr[read_pointer]
            write_pointer -= 1
            read_pointer -= 1
    return arr
