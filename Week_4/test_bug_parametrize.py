import pytest

class Bug:
    def __init__(self, id, title, status, severity):
        self.id = id
        self.title = title
        self.status = status
        self.severity = severity

    def can_close(self):
        return self.status == "Resolved" and self.severity != "Critical"

@pytest.mark.parametrize("status, severity, expected", [
    ("Resolved", "Major", True),
    ("Resolved", "Minor", True),
    ("Open", "Major", False),
    ("Open", "Critical", False),
    ("Resolved", "Critical", False),
    ("In Progress", "Trivial", False),
])
def test_can_close(status, severity, expected):
    bug = Bug(1, "Test", status, severity)
    assert bug.can_close() == expected