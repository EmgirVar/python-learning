from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    # Заполняем форму
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # Проверяем, что попали в каталог
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")