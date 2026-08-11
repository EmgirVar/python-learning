def classify_bug(severity):
    if severity == "Critical":
        return("Немедленный фикс")
    elif severity == "Major":
        return("Фикс в текущем спринте")
    elif severity == "Minor":
        return("Фикс по возможности")
    elif severity == "Trivial":
        return("В бэклог")
    else:
        return "Неизвестный severity"

def can_close_bug (status, severity):
    if status == "Resolved" and severity != "Critical":
        return True
    else:
        return False


# Создаём баги
bug1_id = 101
bug1_title = "Первый баг"
bug1_severity = "Critical"
bug1_status = "Resolved"

bug2_id = 102
bug2_title = "Второй баг"
bug2_severity = "Minor"
bug2_status = "Open"

bug3_id = 103
bug3_title = "Третий баг"
bug3_severity = "Major"
bug3_status = "In progress"

bug4_id = 104
bug4_title = "Четвертый баг"
bug4_severity = "Trivial"
bug4_status = "Closed"

# Собираем баги в список списков (или список кортежей)
bugs = [
    [bug1_id, bug1_title, bug1_severity, bug1_status],
    [bug2_id, bug2_title, bug2_severity, bug2_status],
    [bug3_id, bug3_title, bug3_severity, bug3_status],
    [bug4_id, bug4_title, bug4_severity, bug4_status]
]

# Цикл обработки

critical_count = 0
major_count = 0
minor_count = 0
trivial_count = 0


for bug in bugs:
    print(f"Баг #{bug[0]}: {bug[1]}")
    print(f"Классификация: {classify_bug(bug[2])}")
    print(f"Можно закрыть: {can_close_bug(bug[3],bug[2])}")

    if bug[2] == "Critical":
        critical_count += 1
    elif bug[2] == "Minor":
        minor_count += 1
    elif bug[2] == "Major":
        major_count += 1
    elif bug[2] == "Trivial":
        trivial_count +=1
  

print("Статистика: ")
print(f"Critical: {critical_count}")
print(f"Major: {major_count}")
print(f"Minor: {minor_count}")
print(f"Trivial: {trivial_count}")



