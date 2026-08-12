# DATA
id_1 = 1
name_1 = "Авторизация пользователя"
priority_1 = "High"
status_1 = "Passed"

id_2 = 2
name_2 = "Прикрепление почты"
priority_2 = "Medium"
status_2 = "Failed"

id_3 = 3
name_3 = "Смена пароля"
priority_3 = "Low"
status_3 = "Blocked"

id_4 = 4
name_4 = "Удаление УЗ"
priority_4 = "Medium"
status_4 = "Not Run"

id_5 = 5
name_5 = "Создание УЗ"
priority_5 = "High"
status_5 = "Failed"

test_cases = [
    [id_1, name_1, priority_1, status_1 ],
    [id_2, name_2, priority_2, status_2 ],
    [id_3, name_3, priority_3, status_3 ],
    [id_4, name_4, priority_4, status_4 ],
    [id_5, name_5, priority_5, status_5 ]
]

#FUNCTION

def format_status(status):
    if status == "Passed":
        return "✅ PASSED"
    elif status == "Failed":
        return "❌ FAILED"
    elif status == "Blocked":
        return "🚫 BLOCKED"
    elif status == "Not Run":
        return "⏳ NOT RUN"
    else:
        return "НЕИЗВЕСТНЫЙ СТАТУС"

def format_priority(priority):
    if priority == "High":
        return "High".upper()
    elif priority == "Medium":
        return "Medium".upper()
    elif priority == "Low":
        return "Low".upper()
    else:
        return "НЕИЗВЕСТНЫЙ ПРИОРИТЕТ"

def generate_report_line(test):
    return f"[{format_priority(test[2])}] TC#{test[0]}: {test[1]} | {format_status(test[3])}"

#TASKS
for test in test_cases:
    print(f"{generate_report_line(test)}")    
print(f"========================================")