#DATA
#СЛОВАРИ
bugs = [
    {
        "id": 1,
        "title": "Первый баг",
        "severity": "Critical",
        "status": "Resolved",
        "assignee": "Ivan"
    },
    {
        "id": 2,
        "title": "Второй баг",
        "severity": "Major",
        "status": "Resolved",
        "assignee": "Ivan"
    },
    {
        "id": 3,
        "title": "Третий баг",
        "severity": "Minor",
        "status": "In Progress",
        "assignee": "Maria"
    },
    {
        "id": 4,
        "title": "Четвертый баг",
        "severity": "Trivial",
        "status": "Closed",
        "assignee": "Alex"
    },
    {
        "id": 5,
        "title": "Пятый баг",
        "severity": "Critical",
        "status": "Open",
        "assignee": "Alex"
    },
    {
        "id": 6,
        "title": "Шестой баг",
        "severity": "Major",
        "status": "In Progress",
        "assignee": "Alex"
    }
]




#FUNCTION
#1
def format_bug(bug):
    return f"[{bug["severity"].upper()}] BUG#{bug["id"]}: {bug["title"]} | Status: {bug["status"].upper()} | Assignee: {bug["assignee"]}"

#2
def count_by_assignee(bugs, name):
    count =  0
    for bug in bugs:
        if bug["assignee"] == name:
            count += 1
    return count


#3
def get_critical_open(bugs):
    count = 0
    for bug in bugs:
        if bug["severity"] == "Critical" and bug["status"] == "Open":
            count += 1
    return count

#4
def get_critical_name(bugs):
    result = []
    for bug in bugs:
        if bug["severity"] == "Critical" and bug["status"] == "Open":
            result.append(bug["title"])
    return result

#4
def is_release_ready(bugs):
    if get_critical_open(bugs) == 0:
        return True
    else:
        return False




#TASKS
print(f"=== MINI TMS REPORT V2 ===")
for bug in bugs:
    print(f"{format_bug(bug)}")
print()

print(f"=== WORKLOAD ===")
print(f"Ivan: {count_by_assignee(bugs, "Ivan")}")
print(f"Alex: {count_by_assignee(bugs, "Alex")}")
print(f"Maria: {count_by_assignee(bugs, "Maria")}")
print()

print(f"=== CRITICAL OPEN BUGS ===")
print(f"FOUND: {get_critical_open(bugs)}")
print(f"List: {get_critical_name(bugs)}")
print()

print(f"=== RELEASE STATUS ===")
print(f"Release ready: {is_release_ready(bugs)}")