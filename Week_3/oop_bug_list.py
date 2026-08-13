class Bug:
    def __init__(self, id, title, severity, status, assignee):
        self.id = id
        self.title = title
        self.severity = severity
        self.status = status
        self.assignee = assignee

    def format_bug(self):
        return f"[{self.severity.upper()}] BUG#{self.id}: {self.title} | Status: {self.status.upper()} | Assignee: {self.assignee}"

bugs = [
    Bug(101, "500 на оплате", "Critical", "Open", "Ivan"),
    Bug(102, "Кнопка не активна", "Major", "Resolved", "Maria"),
    Bug(103, "Ошибка валидации", "Minor", "In Progress", "Alex"),
    Bug(104, "Пустая страница", "Critical", "Resolved", "Ivan"),
    Bug(105, "Медленная загрузка", "Trivial", "Open", "Maria")
]

all_bugs = len(bugs)

for bug in bugs:
    print(bug.format_bug())

print(f"====")

def get_critical_count(bugs):
    count = 0
    for bug in bugs:
        if bug.severity == "Critical":
            count += 1
    return count

def get_critical_names(bugs):
    result =[]
    for bug in bugs:
        if bug.severity == "Critical":
            result.append(bug.title)
    return result

def get_bugs_by_assignee(bugs, name):
    result = []
    for bug in bugs:
        if bug.assignee == name:  
            result.append(bug)     
    return result

ivan_bugs = get_bugs_by_assignee(bugs, "Ivan")
print(f"\n=== Ivan's bugs ===")
print(f"Count: {len(ivan_bugs)}")
for bug in ivan_bugs:
    print(bug.format_bug())
print(f"")
maria_bugs = get_bugs_by_assignee(bugs, "Maria")
print(f"\n=== Maria's bugs ===")
print(f"Count: {len(maria_bugs)}")
for bug in maria_bugs:
    print(bug.format_bug())
print(f"")
alex_bugs = get_bugs_by_assignee(bugs, "Alex")
print(f"\n=== Alex's bugs ===")
print(f"Count: {len(alex_bugs)}")
for bug in alex_bugs:
    print(bug.format_bug())
print(f"")
print(f"Общее количество багов: {all_bugs}")
print(f"Число критичных багов: {get_critical_count(bugs)}")
print(f"List: {get_critical_name(bugs)}")
print(f"====")
