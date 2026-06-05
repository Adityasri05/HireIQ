"""
Scoring Engine — calculates the weighted Hirevium score.

Technical Competency = 35%
Knowledge Depth = 20%
Communication = 15%
Pressure Handling = 10%
Skill Verification = 10%
Time Efficiency = 5%
Confidence = 5%
"""


def calculate_hirevium_score(
    technical: float,
    knowledge_depth: float,
    communication: float,
    pressure: float,
    skill_verification: float,
    time_efficiency: float,
    confidence: float,
) -> float:
    """Calculate the weighted Hirevium score (0-100)."""
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


def calculate_hire_probability(hirevium_score: float) -> float:
    """Convert Hirevium score to a hire probability percentage."""
    if hirevium_score >= 85:
        return round(min(90 + (hirevium_score - 85) * 0.67, 99), 1)
    elif hirevium_score >= 70:
        return round(60 + (hirevium_score - 70) * 2, 1)
    elif hirevium_score >= 50:
        return round(30 + (hirevium_score - 50) * 1.5, 1)
    else:
        return round(max(hirevium_score * 0.6, 5), 1)


def get_recommendation(hirevium_score: float) -> str:
    """Get hiring recommendation based on Hirevium score."""
    if hirevium_score >= 85:
        return "Strong Hire"
    elif hirevium_score >= 70:
        return "Hire"
    elif hirevium_score >= 55:
        return "Borderline"
    elif hirevium_score >= 40:
        return "Needs Improvement"
    else:
        return "Reject"
