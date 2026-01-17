def unemployment_rate(unemployed, employed):
    """Повернути рівень безробіття (РБ) як частку від 1.

       Розрахунок за формулою: РБ = безробітні / (зайняті + безробітні).
    """
    if unemployed + employed == 0:
        raise ZeroDivisionError("Сума зайнятих і безробітних не може дорівнювати нулю")
    return unemployed / (unemployed + employed)


try:
    unemployed = int(input("Введіть кількість безробітних (людей): "))
    employed = int(input("Введіть кількість зайнятих (людей): "))
    rate = unemployment_rate(unemployed, employed)
    print(f"Рівень безробіття = {rate:.1%}")

except ValueError:
    print("Помилка: потрібно вводити цілі числа")

except ZeroDivisionError as e:
    print("Помилка:", e)
