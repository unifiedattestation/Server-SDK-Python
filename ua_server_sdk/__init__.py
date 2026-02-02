import json
import urllib.request
from typing import Dict, List, Optional


def _normalize(base_url: str) -> str:
    return base_url[:-1] if base_url.endswith("/") else base_url


def get_backend_info(base_url: str) -> Dict:
    url = f"{_normalize(base_url)}/api/v1/info"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def decode_token(
    base_url: str,
    api_secret: str,
    project_id: str,
    token: str,
    expected_request_hash: Optional[str] = None,
) -> Dict:
    url = f"{_normalize(base_url)}/api/v1/app/decodeToken"
    payload = {
        "projectId": project_id,
        "token": token,
        "expectedRequestHash": expected_request_hash,
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "x-ua-api-secret": api_secret},
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def get_trusted_backends(base_url: str) -> List[str]:
    url = f"{_normalize(base_url)}/api/v1/info/trusted-backends"
    with urllib.request.urlopen(url) as response:
        payload = json.loads(response.read().decode("utf-8"))
        return payload.get("backendIds", [])
