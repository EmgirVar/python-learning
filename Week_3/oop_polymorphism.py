class Bug:
    def __init__(self, id, title, status, severity):
        self.id = id
        self.title = title
        self.status = status
        self.severity = severity

    def can_close(self):
        return self.status == "Resolved"

    def format(self):
        return f"BUG#{self.id}: {self.title} [{self.severity}]"

class CriticalBug(Bug):
    def can_close(self):
        return False


class MinorBug(Bug):
    def can_close(self):
        return self.status == "Resolved" and self.severity == "Minor"


normal = Bug(101, "Обычный баг", "Resolved", "Major")
critical = CriticalBug(102, "Падение сервера", "Resolved", "Critical")
minor = MinorBug(103, "Опечатка", "Resolved", "Minor")
minor_open = MinorBug(104, "Опечатка 2", "Open", "Minor")

for bug in [normal, critical, minor, minor_open]:
    print(f"{bug.format()} | Can close: {bug.can_close()}")