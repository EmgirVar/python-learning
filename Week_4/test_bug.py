class Bug:
    def __init__(self, id, title, status, severity):
        self.id = id
        self.title = title
        self.status = status
        self.severity = severity
        


    def format_bug(self):
        return f"[{self.severity.upper()}] BUG#{self.id}: {self.title} | Status: {self.status.upper()} | Assignee: {self.assignee}"

    def is_critical(self):
        return self.severity == "Critical"

    def can_close(self):
        if self.status == "Resolved" and self.severity != "Critical":
            return True
        else:
            return False

def test_resolved_bug_can_close():
    bug = Bug(101, "Обычный баг", "Resolved", "Major")
    assert bug.can_close() == True

def test_open_bug_cannot_close():
    bug = Bug(102, "Открытый баг", "Open", "Major")
    assert bug.can_close() == False

def test_resolved_critical_bug():
    bug = Bug(103, "Критичный", "Resolved", "Critical")
    assert bug.can_close() == False