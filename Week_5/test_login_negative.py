from playwright.sync_api import Page, expect

def test_locked_user(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_role("heading", name="Epic sadface: Sorry, this user has been locked out.")).to_be_visible()

def test_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()

    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_role("heading", name="Epic sadface: Username and password do not match any user in this service")).to_be_visible()
