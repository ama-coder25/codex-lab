"""Utility functions for number lists."""

def sort_descending(numbers):
    """Return a new list with the numbers sorted in descending order.

    Args:
        numbers (list): List of numbers to sort.

    Returns:
        list: Numbers sorted from highest to lowest.
    """
    return sorted(numbers, reverse=True)


if __name__ == "__main__":
    example = [5, 1, 3, 2, 4]
    print(sort_descending(example))
