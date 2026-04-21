import pytest
import httpx
import uuid

from giclient.client import AsyncClientAPI

# Ensure pytest uses asyncio
pytestmark = pytest.mark.asyncio


async def test_live_sandbox_authentication(sandbox_client: AsyncClientAPI) -> None:
    """
    Triggers the authentication flow against the sandbox and 
    verifies it successfully retrieves data.
    """
    response = await sandbox_client.businesses.current()
    
    assert isinstance(response, dict), "Response should be a dictionary"


async def test_live_sandbox_create_client(sandbox_client: AsyncClientAPI) -> None:
    """
    Tests creating a client in the sandbox environment using the clients.add method.
    """
    # Generate a unique string to prevent Morning from throwing a 400 Duplicate Error
    unique_id = str(uuid.uuid4())[:8]
    
    payload = {
        "name": f"Test Sandbox Client {unique_id}",
        "emails": [f"test_{unique_id}@example.com"]
    }
    
    try:
        response = await sandbox_client.clients.add(**payload)
        
        assert isinstance(response, dict), "Response should be a dictionary"
        assert "id" in response, "Expected an 'id' to be generated for the new client"
        assert response.get("name") == payload["name"], "Client name did not match the payload"
        
    except httpx.HTTPStatusError as e:
        # Morning returns a detailed JSON body on 400 errors (e.g., {"errorCode": 1002, "errorMessage": "..."})
        # We catch the exception and fail the test with Morning's exact complaint so it is easy to debug.
        try:
            error_details = e.response.json()
            pytest.fail(f"Morning API rejected the payload! Morning's Error Details: {error_details}")
        except Exception:
            # Fallback if the response isn't JSON
            pytest.fail(f"Morning API rejected the payload! Raw response: {e.response.text}")