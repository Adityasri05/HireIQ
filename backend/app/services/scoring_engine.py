"""
Scoring Engine — calculates the weighted HireIQ score.

Technical Competency = 35%
Knowledge Depth = 20%
Communication = 15%
Pressure Handling = 10%
Skill Verification = 10%
Time Efficiency = 5%
Confidence = 5%
"""


def calculate_hireiq_score(
    technical: float,
    knowledge_depth: float,
    communication: float,
    pressure: float,
    skill_verification: float,
    time_efficiency: float,
    confidence: float,
) -> float:
    """Calculate the weighted HireIQ score (0-100)."""
    score = (
        technical * 0.35
        + knowledge_depth * 0.20
        + communication * 0.15
        + pressure * 0.10
        + skill_verification * 0.10
        + time_efficiency * 0.05
        + confidence * 0.05
    )
    return round(min(max(score, 0), 100), 1)


def calculate_hire_probability(hireiq_score: float) -> float:
    """Convert HireIQ score to a hire probability percentage."""
    if hireiq_score >= 85:
        return round(min(90 + (hireiq_score - 85) * 0.67, 99), 1)
    elif hireiq_score >= 70:
        return round(60 + (hireiq_score - 70) * 2, 1)
    elif hireiq_score >= 50:
        return round(30 + (hireiq_score - 50) * 1.5, 1)
    else:
        return round(max(hireiq_score * 0.6, 5), 1)


def get_recommendation(hireiq_score: float) -> str:
    """Get hiring recommendation based on HireIQ score."""
    if hireiq_score >= 85:
        return "Strong Hire"
    elif hireiq_score >= 70:
        return "Hire"
    elif hireiq_score >= 55:
        return "Borderline"
    elif hireiq_score >= 40:
        return "Needs Improvement"
    else:
        return "Reject"
