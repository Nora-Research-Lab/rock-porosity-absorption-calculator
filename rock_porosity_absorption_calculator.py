def calculate_absorption(dry_weight, saturated_weight):
    """Calculate water absorption in percent."""
    if dry_weight <= 0:
        raise ValueError("Dry weight must be positive.")
    return ((saturated_weight - dry_weight) / dry_weight) * 100

def calculate_porosity(dry_weight, saturated_weight, submerged_weight):
    """Calculate apparent porosity in percent."""
    numerator = saturated_weight - dry_weight
    denominator = saturated_weight - submerged_weight
    if denominator <= 0:
        raise ValueError("Saturated weight must be greater than submerged weight.")
    return (numerator / denominator) * 100

def calculate_bulk_density(dry_weight, saturated_weight, submerged_weight):
    """Calculate bulk density in g/cm³."""
    denominator = saturated_weight - submerged_weight
    if denominator <= 0:
        raise ValueError("Saturated weight must be greater than submerged weight.")
    return dry_weight / denominator

def classify_porosity(porosity_value):
    """Classify porosity into categories."""
    if porosity_value < 1:
        return "Very Low"
    elif porosity_value <= 5:
        return "Low"
    elif porosity_value <= 15:
        return "Moderate"
    elif porosity_value <= 30:
        return "High"
    else:
        return "Very High"
