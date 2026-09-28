import pytest
from playwright.sync_api import Page, expect

def test_saucedemo_login(page: Page):
    # 1. Navigate to the Sauce Demo website
    page.goto("https://www.saucedemo.com/")
    
    # 2. Fill in the standard username using the data-test locator
    page.locator("[data-test='username']").fill("standard_user")
    
    # 3. Fill in the password
    page.locator("[data-test='password']").fill("secret_sauce")
    
    # 4. Click the Login button
    page.locator("[data-test='login-button']").click()
    
    # 5. Assert successful login by checking the URL and page header
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_header = page.locator("[data-test='title']")
    expect(inventory_header).to_have_text("Products")

def test_add_item_to_cart(page: Page):
    # 1. Navigate to the Sauce Demo website
    page.goto("https://www.saucedemo.com/")

    # 2. Fill in the standard username using the data-test locator
    page.locator("[data-test='username']").fill("standard_user")

    # 3. Fill in the password
    page.locator("[data-test='password']").fill("secret_sauce")

    # 4. Click the Login button
    page.locator("[data-test='login-button']").click()

    # 5. Click Add to cart button for onesie
    page.locator("[data-test='add-to-cart-sauce-labs-onesie']").click()

    # 6. Navigate to cart
    page.locator("[data-test='shopping-cart-link']").click()

    # 7. Assert correct item is in cart
    expect(page.locator(".inventory_item_name").first).to_have_text("Sauce Labs Onesie")
