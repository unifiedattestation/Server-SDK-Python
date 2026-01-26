# Server-SDK-Python

## Functions
- `get_backend_info(base_url)`
- `decode_token(base_url, api_secret, project_id, token, expected_request_hash=None)`
- `is_backend_trusted(backend_id, trusted_backends)`

## Usage
```python
from ua_server_sdk import get_backend_info, decode_token

info = get_backend_info("http://localhost:3001")
result = decode_token(
    base_url="http://localhost:3001",
    api_secret="<secret>",
    project_id="com.example.app",
    token="<token>",
    expected_request_hash="<sha256>"
)
```
