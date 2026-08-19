from playwright.sync_api import Page, expect

def test_sort_by_price_low_to_high(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator(".product_sort_container").select_option("lohi") # в локаторе поиск по классу!!!

    expect(page.locator(".inventory_item_price").first).to_have_text('$7.99')
    expect(page.locator(".inventory_item_price").nth(3)).to_have_text('$15.99')
    expect(page.locator(".inventory_item_price").last).to_have_text('$49.99')