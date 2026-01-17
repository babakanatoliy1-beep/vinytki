min_grades = {"Історія": 180, "Математика": 185, "Українська мова": 175}

print(
    """Щоб визначити можливість вступу, необхідна інформація про вас.

Щоб ввести іспит і бали, введіть їх через |: Історія | 140.
Щоб завершити введення, натисніть кнопку Enter.
"""
)

exams = {}

while True:
    line = input("").strip()
    if line == "":
        break

    try:
        exam, grade = [x.strip() for x in line.split("|")]
        exams[exam] = int(grade)
    except ValueError:
        print("Помилка введення. Формат: Іспит | Бали")

print("Ваші іспити:")
for i, (exam, grade) in enumerate(exams.items(), start=1):
    print(f"{i}) {exam} {grade}")

ok = True
for exam_name, min_grade in min_grades.items():
    try:
        if exams[exam_name] < min_grade:
            ok = False
            break
    except KeyError:
        ok = False
        break

print("Ви можете вступити до нас!" if ok else "На жаль...")
