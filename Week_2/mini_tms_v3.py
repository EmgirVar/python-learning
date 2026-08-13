import json

with open("bugs.json", "r", encoding="utf-8") as file:
    bugs = json.load(file)

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
def get_critical_open_titles(bugs):
    result = []
    for bug in bugs:
        if bug["severity"] == "Critical" and bug["status"] == "Open":
            result.append(bug["title"])
    return result

#4
def is_release_ready(bugs):
    return len(get_critical_open_titles(bugs)) == 0


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
print(f"FOUND: {get_critical_open_titles(bugs)}")
print(f"List: {get_critical_open_titles(bugs)}")
print()

print(f"=== RELEASE STATUS ===")
print(f"Release ready: {is_release_ready(bugs)}")