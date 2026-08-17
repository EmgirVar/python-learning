class BasePage:
    def __init__(self, url):
        self.url = url

    def open(self):
        return f"Открываем страницу: {self.url}"

    def get_title(self):
        return f"Заголовок: {self.url}"

class LoginPage(BasePage):
    def __init__(self, url, username_field, password_field):
        super().__init__(url)
        self.username_field = username_field
        self.password_field = password_field

    def login(self, username, password):
        return f"Вводим логин '{username}' в поле {self.username_field} и пароль '{password}' в поле {self.password_field}"

class DashboardPage(BasePage):
    def __init__(self, url, welcome_message):
        super().__init__(url)
        self.welcome_message = welcome_message

    def check_welcome(self):
        return f"{self.welcome_message}, пользователь!"

login_page = LoginPage("/login", "input#user", "input#pass")
dashboard = DashboardPage("/dashboard", "Добро пожаловать")

print(login_page.open())
print(login_page.login("test_user", "secret123"))
print(dashboard.open())
print(dashboard.check_welcome())