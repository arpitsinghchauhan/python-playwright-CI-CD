import pytest
from pages.login_page import LoginPage
from core.config import Config

@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(page):
    """TC-01: Verify valid user can login"""
    login_page = LoginPage(page)
    login_page.login(Config.USERNAME, Config.PASSWORD)
    assert login_page.is_inventory_visible(), "Inventory page should be visible after valid login"

@pytest.mark.ui    
def test_invalid_login(page):
    """TC-02: Verify error message on invalid login"""
    login_page = LoginPage(page)
    login_page.login("invalid_user", "invalid_pass")
    error = login_page.get_error_message()
    assert "locked out" in error,f"Expected error message to contain 'locked out', got:{error}"