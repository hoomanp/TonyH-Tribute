"""
Hoare Logic: {P} C {Q}
P: Pre-condition (Must be true before execution)
C: Command (The program code)
Q: Post-condition (Must be true after execution)

This example demonstrates Hoare's contribution to formal methods for program correctness.
"""

def swap(x, y):
    """
    {Pre: x = A, y = B}
    C: (x, y) = (y, x)
    {Post: x = B, y = A}
    """
    # Define pre-conditions (Initial state)
    A, B = x, y
    print(f"Pre-condition: x={x}, y={y}")
    
    # The Command
    x, y = y, x
    
    # Post-condition verification (Formal check)
    assert x == B and y == A, "Hoare Logic post-condition failed!"
    print(f"Command executed: swap(x, y)")
    print(f"Post-condition: x={x}, y={y} (Verified!)")
    
    return x, y

def division(dividend, divisor):
    """
    {Pre: divisor != 0}
    C: result = dividend / divisor
    {Post: result * divisor == dividend}
    """
    # Pre-condition check (Crucial for safety)
    if divisor == 0:
        raise ValueError("Pre-condition failed: Divisor cannot be zero.")
    
    # Command
    result = dividend / divisor
    
    # Post-condition (Formal correctness)
    # Using a small epsilon for floating point comparison
    assert abs(result * divisor - dividend) < 1e-9, "Correctness failed!"
    print(f"Dividing {dividend} by {divisor}: {result} (Verified!)")
    
    return result

if __name__ == "__main__":
    print("--- Hoare Logic Demonstration ---")
    swap(5, 10)
    print()
    division(10, 2)
