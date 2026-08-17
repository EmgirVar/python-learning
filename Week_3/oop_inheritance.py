class TestCase:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def format(self):
        return f"TC#{self.id}: {self.name} | {self.status}"

class ApiTest(TestCase):
    def __init__(self, id, name, status, method, endpoint):
        super().__init__(id, name, status)
        self.method = method
        self.endpoint = endpoint

class UiTest(TestCase):
    def __init__(self, id, name, status, browser):
        super().__init__(id, name, status)
        self.browser = browser


api_test = ApiTest(1, "Авторизация", "Passed", "POST", "/api/login")
ui_test = UiTest(2, "Кнопка оплаты", "Failed", "Chrome")

print(api_test.format())
print(f"Method: {api_test.method}, Endpoint: {api_test.endpoint}")
print("---")
print(ui_test.format())
print(f"Browser: {ui_test.browser}")