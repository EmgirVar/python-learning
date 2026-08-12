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

#Tasks

def calculate_pass_rate(test_cases):
    all_cases = len(test_cases)
    passed_case = 0
    for test in test_cases:
        if test[3] == "Passed":
            passed_case += 1  
    return (passed_case/all_cases)*100



def get_failed_high_priority(test_cases):
    result =[]
    for test in test_cases:
       if test[3] == "Failed" and test[2] == "High":
           result.append(test[1])
    return result

failed = get_failed_high_priority(test_cases)

#RESULT

print(f"=== ПРОЦЕНТ УСПЕШНОСТИ ===")
print(f"Pass rate: {calculate_pass_rate(test_cases)}")
print("")
print(f"=== ПРОВАЛЕННЫЕ ТЕСТЫ С ВЫСОКИМ ПРИОРИТЕТОМ ===")
print(f"Найдено: {len(failed)}")
print(f"Список: {failed}")