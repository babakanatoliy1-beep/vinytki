class NoMoneyToWithdrawError(Exception):
    """Недостатньо коштів для зняття."""
    pass


class PaymentError(Exception):
    """Помилка під час переказу."""
    pass


def print_accounts(accounts):
    """Друк акаунтів."""
    print(f"Список клієнтів ({len(accounts)}): ")
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print(f"{i}. {name} {value}")


def transfer_money(accounts, account_from, account_to, value):
    """Виконати переказ грошей з одного рахунку на інший
    з підтримкою транзакції (відкату у разі помилки).
    """

    if value <= 0:
        raise PaymentError("Некоректна сума переказу")

    if account_from not in accounts or account_to not in accounts:
        raise PaymentError("Один із рахунків не існує")

    if accounts[account_from] < value:
        raise NoMoneyToWithdrawError(
            f"Недостатньо коштів на рахунку '{account_from}'"
        )

    # збереження початкового стану (транзакція)
    old_from = accounts[account_from]
    old_to = accounts[account_to]

    try:
        accounts[account_from] -= value
        accounts[account_to] += value
    except Exception:
        # відкат транзакції
        accounts[account_from] = old_from
        accounts[account_to] = old_to
        raise PaymentError("Помилка під час виконання переказу")


if __name__ == "__main__":
    accounts = {
        "Василь Іванов": 100,
        "Іван Васильєв": 1500,
        "Петро Бондаренко": 400
    }

    print_accounts(accounts)

    payment_info = {
        "account_from": "Василь Іванов",
        "account_to": "Іван Васильєв"
    }

    print(
        "Переказ від {account_from} для {account_to}...".
        format(**payment_info)
    )

    try:
        payment_info["value"] = int(input("Сума = "))
        transfer_money(accounts, **payment_info)
        print("OK!")
    except NoMoneyToWithdrawError as e:
        print("ПОМИЛКА:", e)
    except PaymentError as e:
        print("ПОМИЛКА:", e)

    print_accounts(accounts)class NoMoneyToWithdrawError(Exception):
    """Недостатньо коштів для зняття."""
    pass


class PaymentError(Exception):
    """Помилка під час переказу."""
    pass


def print_accounts(accounts):
    """Друк акаунтів."""
    print(f"Список клієнтів ({len(accounts)}): ")
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print(f"{i}. {name} {value}")


def transfer_money(accounts, account_from, account_to, value):
    """Виконати переказ грошей з одного рахунку на інший
    з підтримкою транзакції (відкату у разі помилки).
    """

    if value <= 0:
        raise PaymentError("Некоректна сума переказу")

    if account_from not in accounts or account_to not in accounts:
        raise PaymentError("Один із рахунків не існує")

    if accounts[account_from] < value:
        raise NoMoneyToWithdrawError(
            f"Недостатньо коштів на рахунку '{account_from}'"
        )

    # збереження початкового стану (транзакція)
    old_from = accounts[account_from]
    old_to = accounts[account_to]

    try:
        accounts[account_from] -= value
        accounts[account_to] += value
    except Exception:
        # відкат транзакції
        accounts[account_from] = old_from
        accounts[account_to] = old_to
        raise PaymentError("Помилка під час виконання переказу")


if __name__ == "__main__":
    accounts = {
        "Василь Іванов": 100,
        "Іван Васильєв": 1500,
        "Петро Бондаренко": 400
    }

    print_accounts(accounts)

    payment_info = {
        "account_from": "Василь Іванов",
        "account_to": "Іван Васильєв"
    }

    print(
        "Переказ від {account_from} для {account_to}...".
        format(**payment_info)
    )

    try:
        payment_info["value"] = int(input("Сума = "))
        transfer_money(accounts, **payment_info)
        print("OK!")
    except NoMoneyToWithdrawError as e:
        print("ПОМИЛКА:", e)
    except PaymentError as e:
        print("ПОМИЛКА:", e)

    print_accounts(accounts)
