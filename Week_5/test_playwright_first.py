from playwright.sync_api import sync_playwright

def test_open_browser():
    with sync_playwright() as p:
        # 1. Запускаем браузер
        browser = p.chromium.launch(headless=False)  # headless=False = видимый браузер
        
        # 2. Создаём новую вкладку
        page = browser.new_page()
        
        # 3. Открываем сайт
        page.goto("https://tapochek.net/")
        
        # 4. Делаем скриншот
        page.screenshot(path="screenshot.png")
        
        # 5. Закрываем браузер
        browser.close()