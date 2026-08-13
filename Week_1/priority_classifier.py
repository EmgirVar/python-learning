def  get_test_duration(priority):
    if priority == "High":
        return 45
    elif priority == "Medium":
        return 30
    elif priority == "Low":
        return 15
    else:
        return 0

def get_risk_level(priority, status):
    if priority == "High" and status == "Failed":
        return "🔴 Критический риск"
    elif priority == "High" and status != "Failed":
        return "🟡 Повышенный риск"
    elif priority == "Medium" and status == "Failed":
        return "🟡 Повышенный риск"
    else:
        return "🟢 Низкий риск"

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

total_time = 0

test_cases = [
    [id_1, name_1, priority_1, status_1 ],
    [id_2, name_2, priority_2, status_2 ],
    [id_3, name_3, priority_3, status_3 ],
    [id_4, name_4, priority_4, status_4 ],
    [id_5, name_5, priority_5, status_5 ]
]

for case in test_cases:
    print(f"TC# {case[0]}: {case[1]}")
    print(f"Приоритет: {case[2]} | Длительность: {get_test_duration(case[2])} | Риск: {get_risk_level(case[2],case[3])}")
    total_time += get_test_duration(case[2])
print(f"Суммарное время кейсов: {total_time}")