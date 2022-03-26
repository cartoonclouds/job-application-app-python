from app.utils.string_functions import rreplace

def format_object_name(*args: str, separator: str = ":") -> str:
    """Constructs a formatted string with hierarchical component names to name an object.

    Args:
        separator (str, optional): Separator of component names. Defaults to ":".

    Returns:
        str: A new object name.
    """
    return rreplace(separator.join(args), separator, "/", 1)
