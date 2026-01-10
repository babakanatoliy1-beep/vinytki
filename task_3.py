def first_vacant_row(seats):
    """Повернути перший ряд,
    в якому є найбільше вільних місць та їх кількість.
    Повертається нумерація рядів із 1.
    Якщо вільних місць немає, повернути 0, 0.
    Параметры: - seats (list of list): інформація про продані квитки
    (1 - продано, 0 - ні). Результат: -
    tuple (ряд, кількість місць). """
    max_count = 0
    max_row = 0

    for row_index, row in enumerate(seats, 1):#Нумерація повинна починатись з 1, а enumerate починає з 0
        available_seats_count = row.count(0)

        if available_seats_count > max_count:#За умовою потрібно перший ряд з максимумом, а >= вибере останній
            max_row = row_index
            max_count = available_seats_count

    if max_count == 0:
        return 0, 0

    return max_row, max_count#Якщо немає вільних місць, потрібно повертати (0, 0) Ця умова не перевіряється