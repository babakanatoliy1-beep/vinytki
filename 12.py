class ValidationError(Exception):
    """Базовий клас для помилок валідації."""
    pass


class InvalidEmailError(ValidationError):
    """Виняток для невалідної електронної пошти."""
    pass


class WeakPasswordError(ValidationError):
    """Виняток для слабкого пароля."""
    pass


class InvalidAgeError(ValidationError):
    """Виняток для невалідного віку."""
    pass


def validate_email(email):
    """Перевірити формат електронної пошти."""
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Некоректний формат email")


def validate_password(password):
    """Перевірити надійність пароля."""
    if len(password) < 8:
        raise WeakPasswordError("Пароль повинен містити щонайменше 8 символів")
    if not any(ch.isdigit() for ch in password):
        raise WeakPasswordError("Пароль повинен містити хоча б одну цифру")


def validate_age(age):
    """Перевірити вік користувача."""
    if age < 14 or age > 120:
        raise InvalidAgeError("Вік повинен бути в діапазоні від 14 до 120")


def register_user(email, password, age):
    """Зареєструвати користувача після валідації."""
    validate_email(email)
    validate_password(password)
    validate_age(age)

    return {
        "email": email,
        "password": password,
        "age": age
    }


if __name__ == "__main__":
    print("=== Реєстрація користувача ===")

    email = input("Email: ")
    password = input("Пароль: ")
    age_str = input("Вік: ")

    try:
        age = int(age_str)
        user = register_user(email, password, age)
        print("✅ Реєстрація успішна!")
        print("Дані користувача:", user)

    except ValidationError as e:
        print("❌ Помилка реєстрації:", e)

    except ValueError:
        print("❌ Вік повинен бути цілим числом")
