import pytest

class Bug:
    def __init__(self, id, title, status, severity):
        self.id = id
        self.title = title
        self.status = status
        self.severity = severity

    def can_close(self):
        return self.status == "Resolved" and self.severity != "Critical"

        
@pytest.fixture
def bug_list():
    return [
        Bug(1, "Баг 1", "Resolved", "Major"),
        Bug(2, "Баг 2", "Open", "Critical"),
        Bug(3, "Баг 3", "Resolved", "Minor")
    ]

def test_list_length(bug_list):
    assert len(bug_list) == 3

def test_first_bug_can_close(bug_list):
    assert bug_list[0].can_close() == True

def test_count_critical(bug_list):
    count = 0
    for bug in bug_list:
        if bug.severity == "Critical":
            count += 1
    assert count == 1
    