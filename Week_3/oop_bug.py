class Bug:
    def __init__(self, id, title, severity, status, assignee):
        self.id = id
        self.title = title
        self.severity = severity
        self.status = status
        self.assignee = assignee


    def format_bug(self):
        return f"[{self.severity.upper()}] BUG#{self.id}: {self.title} | Status: {self.status.upper()} | Assignee: {self.assignee}"

    def is_critical(self):
        return self.severity == "Critical"

    def can_close(self):
        if self.status == "Resolved" and self.severity != "Critical":
            return True
        else:
            return False


bug1 = Bug(101, "500 на оплате", "Critical", "Open", "Ivan")
bug2 = Bug(102, "Кнопка не активна", "Major", "Resolved", "Maria")
bug3 = Bug(103, "Ошибка валидации", "Minor", "In Progress", "Alex")

print(bug1.format_bug())
print(f"Is critical: {bug1.is_critical()}")
print(f"Can close: {bug1.can_close()}")
print("---")

print(bug2.format_bug())
print(f"Is critical: {bug2.is_critical()}")
print(f"Can close: {bug2.can_close()}")
print("---")

print(bug3.format_bug())
print(f"Is critical: {bug3.is_critical()}")
print(f"Can close: {bug3.can_close()}")
print("---")
