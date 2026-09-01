def calculate_health_score(refresh_status, freshness_hours):
    """
    Calculate a health score from 0 to 100.
    """

    score = 100

    if refresh_status.lower() == "failed":
        score -= 50

    if freshness_hours > 4:
        score -= 20

    if freshness_hours > 12:
        score -= 20

    return max(score, 0)


def get_health_status(score):
    """
    Convert a numeric health score into a health status.
    """

    if score >= 90:
        return "Healthy"

    if score >= 70:
        return "Warning"

    return "Critical"
