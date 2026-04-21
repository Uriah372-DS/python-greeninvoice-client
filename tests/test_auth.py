import pytest

from giclient.client import AsyncClientAPI

# Tell pytest to run all async tests in this file correctly
pytestmark = pytest.mark.asyncio


async def test_authentication_flow(sandbox_client: AsyncClientAPI) -> None:
    """
    Tests that the new client_credentials grant type successfully 
    fetches a token from the Morning Sandbox API.
    """
    # 1. Verify the client starts without a token (lazy loading)
    auth_instance = sandbox_client.manager.auth
    assert auth_instance._token is None, "Token should be None before the first request."

    # 2. Trigger the authentication flow by making a safe API call using your wrapper method.
    response: dict = await sandbox_client.businesses.current()
    
    # 3. Verify the wrapper method correctly parsed and returned a dictionary
    assert isinstance(response, dict), f"Expected a dictionary, got {type(response)}"
    
    # 4. Verify that the auth class successfully captured and stored the new token
    assert auth_instance._token is not None, "Authentication token was not saved!"
    assert isinstance(auth_instance._token, str), "Token should be a string."
    assert len(auth_instance._token) > 20, "Token appears suspiciously short or invalid."