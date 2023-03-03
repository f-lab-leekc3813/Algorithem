def solution(n):
    """
    Reverses a natural number n and returns it as an array with each digit as an element.

    Args:
        n (int): A natural number.

    Returns:
        A list of integers where each integer is a single digit of n,
        reversed in order.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a natural number.")
    return [int(char) for char in str(n)[::-1]]