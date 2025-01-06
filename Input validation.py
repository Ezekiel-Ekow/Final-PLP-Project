def is_valid_input(weight):
    """
    Validate user input for weight.
    
    Args:
    - weight (float): Weight input.
    
    Returns:
    - bool: True if valid, False otherwise.
    """
    try:
        weight = float(weight)
        if weight <= 0:
            return False
        return True
    except ValueError:
        return False
