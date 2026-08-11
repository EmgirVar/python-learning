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
status_5 = "Passed"

test_cases = [
    [id_1, name_1, priority_1, status_1 ],
    [id_2, name_2, priority_2, status_2 ],
    [id_3, name_3, priority_3, status_3 ],
    [id_4, name_4, priority_4, status_4 ],
    [id_5, name_5, priority_5, status_5 ]
]

all_case = len(test_cases)
case_passed = 0
case_failed = 0
case_blocked = 0
case_not_run = 0

for test in test_cases:
    print(f"ТС#{test[0]}: {test[1]} | Приоритет: {test[2]} | Статус: {test[3]}")
    if test[3] == "Passed": 
        case_passed += 1
    elif test[3] == "Failed":
        case_failed += 1
    elif test[3] == "Blocked":
        case_blocked += 1
    elif test[3] == "Not Run":
        case_not_run += 1
    else:
        print(f"⚠️ Неизвестный статус: {test[3]}")

print("=== ИТОГИ ПРОГОНА ===")
print(f"Всего тестов: {all_case}")
print(f"Passed: {case_passed}")
print(f"Failed: {case_failed}")
print(f"Blocked: {case_blocked}")
print(f"Not Run: {case_not_run}")