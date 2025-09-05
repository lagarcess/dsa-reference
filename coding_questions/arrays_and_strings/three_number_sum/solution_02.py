def threeNumberSum(array, targetSum):
    triplets = []
    # O(n) operation to create the set for fast lookups
    num_set = set(array)

    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            current_sum = array[i] + array[j]
            potential_match = targetSum - current_sum

            # Check if the needed number exists in the set and is not one of the current numbers
            if (
                potential_match in num_set
                and potential_match != array[i]
                and potential_match != array[j]
            ):
                triplet = sorted([array[i], array[j], potential_match])
                if triplet not in triplets:
                    triplets.append(triplet)

    return sorted(triplets)
