def power(x, y=2):
    """Повернути x^y."""
    if y < 0:
        raise ValueError("Степінь не може бути від’ємною")
    if y == 0:
        return 1
    return x * power(x, y - 1)


try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError:
    print("Помилка: введіть цілі числа, а степінь має бути ≥ 0.")
except RecursionError:
    print("Помилка: занадто велика або неправильна степінь.")
