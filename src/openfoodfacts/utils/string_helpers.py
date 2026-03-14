def clean_string(s: str) -> str:
    """
    Cleans a string by stripping whitespace and converting to lowercase.

    Args:
        s (str): Input string.

    Returns:
        str: Cleaned string or None if input is None.
    """
    return s.strip().lower() if s else s