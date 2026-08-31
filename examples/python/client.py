import requests
from typing import Optional, Dict, Any, List

class TraffyExchangeClient:
    def __init__(self, base_url: str = "https://publicapi.traffy.in.th/exchange-api"):
        self.base_url = base_url
        self.token: Optional[str] = None

    def authenticate(self, username: str, password: str) -> Dict[str, Any]:
        url = f"{self.base_url}/get-auth/v1"
        res = requests.post(url, json={"user": username, "pass": password})
        res.raise_for_status()
        data = res.json()
        if data.get("status") == "success" and data.get("results"):
            self.token = data["results"][0]["token"]
        return data

    def _get_headers(self) -> Dict[str, str]:
        if not self.token:
            raise ValueError("Client is not authenticated. Call authenticate() first.")
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_issues(self, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}/get-issues/v1"
        res = requests.post(url, json=kwargs, headers=self._get_headers())
        res.raise_for_status()
        return res.json()

    def get_issue(self, ticket_id: Optional[str] = None, client_ticket_id: Optional[str] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/get-issue/v1"
        payload = {}
        if ticket_id:
            payload["ticket_id"] = ticket_id
        if client_ticket_id:
            payload["client_ticket_id"] = client_ticket_id
        res = requests.post(url, json=payload, headers=self._get_headers())
        res.raise_for_status()
        return res.json()

    def new_issue(self, description: str, latitude: float, longitude: float, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}/new-issue/v1"
        payload = {
            "description": description,
            "latitude": latitude,
            "longitude": longitude,
            **kwargs
        }
        res = requests.post(url, json=payload, headers=self._get_headers())
        res.raise_for_status()
        return res.json()

    def update_issue(self, state: str, ticket_id: Optional[str] = None, client_ticket_id: Optional[str] = None, note: Optional[str] = None, photo: Optional[List[str]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/update-issue/v1"
        payload = {"state": state}
        if ticket_id:
            payload["ticket_id"] = ticket_id
        if client_ticket_id:
            payload["client_ticket_id"] = client_ticket_id
        if note:
            payload["note"] = note
        if photo:
            payload["photo"] = photo
        res = requests.post(url, json=payload, headers=self._get_headers())
        res.raise_for_status()
        return res.json()
