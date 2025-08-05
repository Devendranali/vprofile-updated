# test_login.py

import pytest
import time
from playwright.sync_api import Page
from locators.TestLoc import Test_loc

@pytest.mark.smoke
def test_login(page: Page):
    page.goto("http://192.168.49.2:30080/")  # Replace with your actual Minikube IP + port if dynamic
    loc = Test_loc(page)
    loc.username.fill("admin_vp")
    loc.password.fill("admin_vp")
    loc.submit.click()
    
    time.sleep(3)  # Give the page time to load
    assert "dashboard" in page.url or page.url != "http://192.168.49.2:30080/"
