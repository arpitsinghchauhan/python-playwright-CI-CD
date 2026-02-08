import pytest
from core.api_client import APIClient
from data.models import UserResponse

@pytest.mark.api
def test_get_single_user():
    """ Verify GET /users/2 returns valid schema structure"""
    client  = APIClient()
    response = client.get("users/2")
    #Assertion 1
    assert response.status_code == 200

    #Assertion 2 - Schema validation (Pydantic)
    #The ensures fields like 'email' are actually email and id are integers'
    user_data = UserResponse(**response.json())
    assert user_data.data.id == 2, f"Expected user id to be 2, got {user_data.data.id}"
    assert user_data.data.first_name == "Janet", f"Expected first name to be 'Janet', got {user_data.data.first_name}"
