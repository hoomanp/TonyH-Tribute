def quicksort(arr):
    """
    Sir Tony Hoare's Quicksort algorithm (recursive implementation).
    Time Complexity: O(n log n) average, O(n^2) worst case.
    Space Complexity: O(log n) for recursion stack.
    """
    if len(arr) <= 1:
        return arr
    
    # Selecting the pivot (here, the middle element for better average performance)
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    # Example usage
    sample_data = [3, 6, 8, 10, 1, 2, 1]
    sorted_data = quicksort(sample_data)
    print(f"Original: {sample_data}")
    print(f"Sorted:   {sorted_data}")
