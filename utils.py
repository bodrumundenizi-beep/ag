"""
A simple utility module for text formatting and basic data processing.
"""

def clean_text(text: str) -> str:
    """Removes extra whitespace and capitalizes the first letter."""
    if not text:
        return ""
    return " ".join(text.split()).capitalize()

def calculate_stats(numbers: list[float]) -> dict:
    """Returns basic statistics for a list of numbers."""
    if not numbers:
        return {"count": 0, "average": 0, "max": 0, "min": 0}
    
    return {
        "count": len(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

if __name__ == "__main__":
    # Quick self-test
    sample_text = "  hello   world from python!   "
    print("Cleaned:", clean_text(sample_text))
    
    sample_nums = [10, 20, 30, 40, 50]
    print("Stats:", calculate_stats(sample_nums))
