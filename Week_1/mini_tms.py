#DATA

bug1_id = 1
bug1_title = "Первый баг"
bug1_severity = "Critical"
bug1_status = "Resolved"
bug1_assignee = "Ivan"

bug2_id = 2
bug2_title = "Второй баг"
bug2_severity = "Major"
bug2_status = "Resolved"
bug2_assignee = "Ivan"

bug3_id = 3
bug3_title = "Третий баг"
bug3_severity = "Minor"
bug3_status = "In Progress"
bug3_assignee = "Maria"

bug4_id = 4
bug4_title = "Четвертый баг"
bug4_severity = "Trivial"
bug4_status = "Closed"
bug4_assignee = "Alex"

bug5_id = 5
bug5_title = "Пятый баг"
bug5_severity = "Critical"
bug5_status = "Open"
bug5_assignee = "Alex"

bug6_id = 6
bug6_title = "Шестой баг"
bug6_severity = "Major"
bug6_status = "In Progress"
bug6_assignee = "Alex"

bugs = [
    [bug1_id, bug1_title, bug1_severity, bug1_status, bug1_assignee],
    [bug2_id, bug2_title, bug2_severity, bug2_status, bug2_assignee],
    [bug3_id, bug3_title, bug3_severity, bug3_status, bug3_assignee],
    [bug4_id, bug4_title, bug4_severity, bug4_status, bug4_assignee],
    [bug5_id, bug5_title, bug5_severity, bug5_status, bug5_assignee],
    [bug6_id, bug6_title, bug6_severity, bug6_status, bug6_assignee]
]

#FUNCTION
#1
def format_bug(bug):
    return f"[{bug[2].upper()}] BUG#{bug[0]}: {bug[1]} | Status: {bug[3].upper()} | Assignee: {bug[4]}"

#2
def count_by_assignee(bugs, name):
    count =  0
    for bug in bugs:
        if bug[4] == name:
            count += 1
    return count


#3
def get_critical_open(bugs):
    count = 0
    for bug in bugs:
        if bug[2] == "Critical" and bug[3] == "Open":
            count += 1
    return count

#4
def get_critical_name(bugs):
    result = []
    for bug in bugs:
        if bug[2] == "Critical" and bug[3] == "Open":
            result.append(bug[1])
    return result

#4
def is_release_ready(bugs):
    if get_critical_open(bugs) == 0:
        return True
    else:
        return False




#TASKS
print(f"=== MINI TMS REPORT ===")
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