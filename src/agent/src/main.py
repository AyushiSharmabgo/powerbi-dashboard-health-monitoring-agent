from monitoring.health_score import (
    calculate_health_score,
    get_health_status,
)
from agent.health_agent import PowerBIHealthAgent


def main():
    # Simulated Power BI health data.
    # This will later be replaced by Power BI REST API data.
    health_data = {
        "dashboard": "Digital Marketing Dashboard",
        "refresh_status": "Failed",
        "freshness_hours": 9,
        "data_source_status": "Connection Timeout",
    }

    score = calculate_health_score(
        health_data["refresh_status"],
        health_data["freshness_hours"],
    )

    status = get_health_status(score)

    agent = PowerBIHealthAgent()
    analysis = agent.analyze(health_data)

    print("=" * 60)
    print("POWER BI DASHBOARD HEALTH MONITOR")
    print("=" * 60)

    print(f"Dashboard: {health_data['dashboard']}")
    print(f"Health Score: {score}/100")
    print(f"Health Status: {status}")
    print(f"Severity: {analysis['severity']}")

    print("\nIssues:")
    for issue in analysis["issues"]:
        print(f"  - {issue}")

    print("\nRecommendations:")
    for recommendation in analysis["recommendations"]:
        print(f"  - {recommendation}")

    print("=" * 60)


if __name__ == "__main__":
    main()
