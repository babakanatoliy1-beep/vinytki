def transfer_money(accounts, account_from, account_to, value):
    """Виконати переказ 'value' грошей з рахунку 'account_from' на 'account_to'."""
    try:
        if value <= 0:
            raise PaymentError("Некоректна сума")

        if account_from not in accounts or account_to not in accounts:
            raise PaymentError("Рахунок не знайдено")

        if accounts[account_from] < value:
            raise NoMoneyToWithdrawError(
                f"Недостатньо коштів на рахунку {account_from}"
            )

        # зберігаємо стан (транзакція)
        old_from = accounts[account_from]
        old_to = accounts[account_to]

        try:
            accounts[account_from] -= value
            accounts[account_to] += value
        except Exception:
            # відкат транзакції
            accounts[account_from] = old_from
            accounts[account_to] = old_to
            raise PaymentError("Помилка під час переказу")

    except (NoMoneyToWithdrawError, PaymentError) as e:
        print("ПОМИЛКА:", e)
        raise
