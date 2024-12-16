def calculate_runoff(rainfall, cn):
    """
    Calculate runoff using SCS-CN method.
    
    Args:
        rainfall (float): Rainfall in mm.
        cn (float): Curve Number (0-100).
    
    Returns:
        float: Runoff in mm.
    """
    if rainfall <= 0:
        return 0.0

    s = (25400 / cn) - 254  # Maximum potential retention (mm)
    runoff = (rainfall - 0.2 * s)**2 / (rainfall + 0.8 * s) if rainfall > 0.2 * s else 0.0
    return max(runoff, 0.0)
