def f(x):
    """Повернути значення функції.

    Функція не обробляє винятки.
    """
    return x**2 / (x + 2) - 3


try:
    k = int(input("Введіть межу інтервалу [-k; k]: "))
    h = float(input("Введіть крок: "))
    if h == 0:
        raise ValueError
except ValueError:
    print("Помилка введення даних.")
    exit()

x = -k
print("x".rjust(10), "f(x)".rjust(10))

while x <= k:
    try:
        try:
            y = f(x)
            print(f"{x:10.2f} {y:10.2f}")
        except ZeroDivisionError:
            print(f"{x:10.2f} {'-':>10}")
    finally:
        x += h
