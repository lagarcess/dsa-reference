def twoSumIndex(nums: list[int], target: int) -> list[int]:
        # Stores {number: index}
        num_map = {}
        # Iterate through the array with both index and value
        for idx, num in enumerate(nums):
            # Calculate the complement
            y = target - num
            if y in num_map:
                # If the complement exists, return the indices
                # Note: This assumes the input is guaranteed to have exactly one solution
                return [num_map[y], idx]
            # Store the current number and its index
            # This allows us to find the complement in future iterations
            num_map[num] = idx
