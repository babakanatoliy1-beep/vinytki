try:
    n = int(input("Введіть кількість людей: "))
except ValueError:
    print("Помилка: потрібно ввести ціле число.")
    exit()

middle_names = {}
count_used = 0  # скільки людей реально враховано

for i in range(n):
    fio = input("Введіть ПІБ через пробіл: ").split()

    try:
        middle_name = fio[2]   # по-батькові — третє слово
        middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        count_used += 1
    except IndexError:
        # якщо по-батькові немає — просто пропускаємо людину
        print("По-батькові відсутнє, людина не врахована.")

try:
    most_common = sorted(
        middle_names.items(),
        key=lambda item: item[1]
    )[-1][0]

    print("Найпоширеніше по-батькові:", most_common)
    print("Людей брало участь у розрахунку:", count_used)

except IndexError:
    print("Неможливо виконати розрахунок: немає жодної людини з по-батькові.")
