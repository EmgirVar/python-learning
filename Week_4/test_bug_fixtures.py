import pytest

class Bug:
    def __init__(self, id, title, status, severity):
        self.id = id
        self.title = title
        self.status = status
        self.severity = severity

    def can_close(self):
        if self.status == "Resolved" and self.severity != "Critical":
            return True
        else:
            return False
        
@pytest.fixture 
def resolved_bug():
    return Bug(101, "Обычный", "Resolved", "Major")

@pytest.fixture 
def open_bug():
    return Bug(102, "Открытый", "Open", "Major")

@pytest.fixture 
def resolved_critical_bug():
    return Bug(103, "Критичный", "Resolved", "Critical")


def test_resolved_bug_can_close(resolved_bug):
    assert resolved_bug.can_close() == True

def test_open_bug_cannot_close(open_bug):
    assert open_bug.can_close() == False

def test_resolved_critical_bug(resolved_critical_bug):
    assert resolved_critical_bug.can_close() == False