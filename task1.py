def sum_of_digits(n):
    """Повернути суму цифр менших 5 для позитивного цілого числа `n`.
    Якщо таких цифр немає, повернути 0."""

    c = 0
    while n > 0:
        digit = n % 10
        if digit < 5:
            c += digit
        n //= 10
    return c