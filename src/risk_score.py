def calculate_risk_score(threat_level, vulnerability_level, impact_level):
    """
    Calculate a basic risk score using threat, vulnerability, and impact values.

    Each input should be scored from 1 to 5.
    The final score ranges from 1 to 125.
    """

    if not all(1 <= value <= 5 for value in [threat_level, vulnerability_level, impact_level]):
        raise ValueError("All values must be between 1 and 5.")

    return threat_level * vulnerability_level * impact_level


def classify_risk(score):
    """
    Classify risk score into Low, Medium, High, or Critical.
    """

    if score <= 20:
        return "Low"
    elif score <= 50:
        return "Medium"
    elif score <= 90:
        return "High"
    else:
        return "Critical"


if __name__ == "__main__":
    score = calculate_risk_score(4, 3, 5)
    category = classify_risk(score)

    print(f"Risk Score: {score}")
    print(f"Risk Category: {category}")
