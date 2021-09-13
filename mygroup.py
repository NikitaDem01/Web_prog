groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Никита",
        "surname": "Попов",
        "exams": ["РКПО", "СТ", "ОС"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Артем",
        "surname": "Новиков",
        "exams": ["СП", "ММвБД", "ПвКИС"],
        "marks": [3, 3, 2]
    },
]

avr_mark = int(input("Введите средний балл: "))

def print_students(students, avr_mark):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        marks = 0
        for i in student["marks"]:
            marks = marks + i
        if marks/3 > avr_mark:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_students(groupmates, avr_mark)
