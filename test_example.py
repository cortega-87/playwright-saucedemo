import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_sign_in_link(page: Page):
     page.goto("https://www.saucedemo.com/")

     # 1. Locate the username textbox and fill it
     page.get_by_placeholder("Username").fill("standard_user")

     # 2. Locate the password textbox and fill it
     page.get_by_placeholder("Password").fill("secret_sauce")

     # Click the sign in link.
     page.get_by_role("button", name="Login").click()

     # Expects page to have a title with the name of Products.
     expect(page.get_by_text("Products")).to_be_visible()

    
