class PowerBIHealthAgent:
    """
    AI-powered agent that analyzes Power BI health signals
    and provides an explanation and recommended action.
    """

    def analyze(self, health_data):
        refresh_status = health_data.get("refresh_status", "Unknown")
        freshness_hours = health_data.get("freshness_hours", 0)
        data_source_status = health_data.get(
            "data_source_status", "Unknown"
        )

        issues = []
        recommendations = []

        # Check refresh status
        if refresh_status.lower() == "failed":
            issues.append("Semantic model refresh failed.")
            recommendations.append(
                "Check the refresh error details and retry the refresh."
            )

        # Check data freshness
        if freshness_hours > 12:
            issues.append(
                f"Data is {freshness_hours} hours old."
            )
            recommendations.append(
                "Investigate the refresh schedule and data pipeline."
            )

        # Check data source
        if data_source_status.lower() != "healthy":
            issues.append(
                f"Data source status: {data_source_status}."
            )
            recommendations.append(
                "Check the underlying data source and connectivity."
            )

        # Determine severity
        if len(issues) >= 2:
            severity = "Critical"
        elif len(issues) == 1:
            severity = "Warning"
        else:
            severity = "Healthy"

        return {
            "severity": severity,
            "issues": issues,
            "recommendations": recommendations,
        }
