import os

import requests
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv

load_dotenv()


class PowerBIHealthMonitor:
    """Monitor Power BI semantic model refresh health."""

    POWER_BI_SCOPE = "https://analysis.windows.net/powerbi/api/.default"
    POWER_BI_BASE_URL = "https://api.powerbi.com/v1.0/myorg"

    def __init__(self):
        self.tenant_id = os.getenv("POWERBI_TENANT_ID")
        self.client_id = os.getenv("POWERBI_CLIENT_ID")
        self.client_secret = os.getenv("POWERBI_CLIENT_SECRET")

        if not all(
            [
                self.tenant_id,
                self.client_id,
                self.client_secret,
            ]
        ):
            raise ValueError(
                "Power BI authentication environment variables are missing."
            )

        self.credential = ClientSecretCredential(
            tenant_id=self.tenant_id,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )

    def get_access_token(self):
        """Get an Azure access token for Power BI."""

        token = self.credential.get_token(self.POWER_BI_SCOPE)

        return token.token

    def get_refresh_history(self, workspace_id, dataset_id):
        """Get refresh history for a Power BI semantic model."""

        token = self.get_access_token()

        url = (
            f"{self.POWER_BI_BASE_URL}/"
            f"groups/{workspace_id}/"
            f"datasets/{dataset_id}/"
            f"refreshes"
        )

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()
