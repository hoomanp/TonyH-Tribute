from typing import Optional

"""
The "Billion Dollar Mistake":
In 2009, Sir Tony Hoare famously called his invention of the 
null reference his "billion-dollar mistake."

Modern approach in Python:
Use Type Hinting (Optional / Union[T, None]) to explicitly 
handle missing data.
"""

def unsafe_llm_call(prompt: str):
    """A simulation of a function that returns 'None' without handling it."""
    # Simulation: LLM fails to generate a response
    return None

def safer_llm_call(prompt: str) -> Optional[str]:
    """A simulation of a function that explicitly defines it could return None."""
    # Simulation: Explicitly handles failures or empty responses
    return None

def process_unsafe():
    print("--- Unsafe Example ---")
    response = unsafe_llm_call("Translate 'Hello'")
    try:
        # This will crash because response is None
        print(f"Result: {response.upper()}") 
    except AttributeError as e:
        print(f"CRASHED! Error: {e}")
        print("This is the 'Billion Dollar Mistake' in action.")

def process_safer():
    print("\n--- Safer Example (Modern Practice) ---")
    response: Optional[str] = safer_llm_call("Translate 'Hello'")
    
    # Modern practice: Explicitly check for None
    if response is not None:
        print(f"Result: {response.upper()}")
    else:
        print("Safely handled 'None' case. No crash.")

if __name__ == "__main__":
    process_unsafe()
    process_safer()
