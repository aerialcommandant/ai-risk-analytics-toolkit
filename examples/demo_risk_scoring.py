from src.risk_score import calculate_risk_score, classify_risk


sample_cases = [
    {"asset": "Payment System", "threat": 5, "vulnerability": 4, "impact": 5},
    {"asset": "Branch Network", "threat": 3, "vulnerability": 3, "impact": 4},
    {"asset": "AI Model Pipeline", "threat": 4, "vulnerability": 5, "impact": 5},
]


for case in sample_cases:
    score = calculate_risk_score(
        case["threat"],
        case["vulnerability"],
        case["impact"]
    )

    category = classify_risk(score)

    print(f"{case['asset']}: {score} - {category}")
