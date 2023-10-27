def is_number(value):
    """Verifica si el valor es un número."""
    try:
        float(value)
        return True
    except ValueError:
        return False
