import os
from typing import Any, AsyncGenerator
import pytest
from dotenv import load_dotenv
from yarl import URL
from giclient.client import AsyncClientAPI

load_dotenv()

@pytest.fixture
async def sandbox_client() -> AsyncGenerator[AsyncClientAPI, Any, None]:
    """
    Provides an instantiated AsyncClientAPI pointing at Morning's Sandbox environment.
    """
    api_key = os.getenv("MORNING_SANDBOX_API_KEY")
    api_secret = os.getenv("MORNING_SANDBOX_API_SECRET")
    
    if not api_key or not api_secret:
        pytest.skip("Sandbox credentials not found in .env")

    # Explicitly pass the Sandbox Base URL
    sandbox_url = URL("https://sandbox.d.greeninvoice.co.il/api/v1")
    
    async with AsyncClientAPI(api_key=api_key, api_secret=api_secret, base_url=sandbox_url) as client:
        yield client