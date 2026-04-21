import pytest
import httpx
import uuid

from giclient.client import AsyncClientAPI

# Ensure pytest uses asyncio
pytestmark = pytest.mark.asyncio


async def test_live_sandbox_create_item(sandbox_client: AsyncClientAPI) -> None:
    """
    Tests creating an item (product/service) in the catalog.
    """
    unique_id = str(uuid.uuid4())[:8]
    
    payload = {
        "name": f"Test Automation Service {unique_id}",
        "description": "Standard integration test item.", # Added missing required field
        "price": 500.0,
        "currency": "ILS",
        "vatType": 0  # 0 usually denotes standard VAT rate
    }
    
    try:
        response = await sandbox_client.items.add(**payload)
        
        assert isinstance(response, dict), "Response should be a dictionary"
        assert "id" in response, "Expected an 'id' to be generated for the new item"
        assert response.get("name") == payload["name"], "Item name did not match the payload"
        
    except httpx.HTTPStatusError as e:
        await e.response.aread()
        try:
            error_details = e.response.json()
            pytest.fail(f"Morning API rejected the item payload! Error Details: {error_details}")
        except Exception:
            pytest.fail(f"Morning API rejected the item payload! Raw response: {e.response.text}")


async def test_live_sandbox_create_document(sandbox_client: AsyncClientAPI) -> None:
    """
    Tests creating a document by first generating a temporary client.
    """
    unique_id = str(uuid.uuid4())[:8]
    
    # 1. First, create a temporary client to attach the invoice to
    client_payload = {
        "name": f"Doc Target Client {unique_id}",
        "emails": [f"target_{unique_id}@example.com"]
    }
    
    try:
        client_response = await sandbox_client.clients.add(**client_payload)
        client_id = client_response["id"]
    except httpx.HTTPStatusError as e:
        await e.response.aread()
        pytest.fail(f"Failed to create prerequisite client for document test. Error: {e.response.text}")

    # 2. Next, create the document (Type 300 = Price Quote / Haza'at Mechir)
    doc_payload = {
        "description": f"API Test Quote {unique_id}",
        "type": 300,
        "lang": "he", # Explicitly set the language to Hebrew
        "currency": "ILS", # Master currency for the entire document
        "client": {
            "id": client_id
        },
        "income": [
            {
                "description": "Consulting Hours",
                "quantity": 2,
                "price": 250.0,
                "currency": "ILS",
                "vatType": 0
            }
        ]
    }
    
    try:
        doc_response = await sandbox_client.documents.add(**doc_payload)
        
        assert isinstance(doc_response, dict), "Response should be a dictionary"
        assert "id" in doc_response, "Expected an 'id' to be generated for the new document"
        assert "documentNumber" in doc_response or "number" in doc_response, "Expected a document number in the response"
        
    except httpx.HTTPStatusError as e:
        await e.response.aread()
        try:
            error_details = e.response.json()
            pytest.fail(f"Morning API rejected the document payload! Error Details: {error_details}")
        except Exception:
            pytest.fail(f"Morning API rejected the document payload! Raw response: {e.response.text}")