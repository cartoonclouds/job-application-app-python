def rreplace(s: str, old: str, new: str, count: int = -1) -> str:
    """Return a copy of string _s_ with all occurrences of substring
    _old_ replaced by _new_, replacing the substring from the right.

    Args:
        s (str): Text string to make replacements on.
        old (str): String to find.
        new (str): String to replace _old_ with.
        count (int, optional): Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.. Defaults to -1.

    Returns:
        str: A new string with replacements.
    """
    return s if count == 0 else new.join(s.rsplit(old, count))
