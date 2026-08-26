# Проект FitLife - MVP версия 1.0
# Количество воды, необходимое на 1 кг веса человека, в мл
WATER_PER_KILO = 30
# Количество мл в 1 л воды
WATER_ML_PER_LITRE = 1000


def welcome_user():
    """Приветствует пользователя, спрашивает его имя и возраст.

    Returns:
        name: Имя пользователя.
        age: Возраст пользователя.
    """
    print("Приветсвуем вас в нашем приложении FitLife!")
    user_name = input("Введите ваше имя: ").title()
    print(f"Привет, {user_name}!")
    user_age = int(input("Введите ваш возраст в годах (например, 23): "))
    return user_name, user_age


def get_user_info():
    """Спрашивает вес и рост пользователя.

    Returns:
        weight: Вес пользователя в килограммах.
        height: Рост пользователя в метрах.
    """
    user_weight = float(input("Введите ваш вес в кг (56 или 56.2): "))
    user_height = float(input("Введите ваш рост в метрах (например, 1.7): "))
    return user_weight, user_height


def calculate_bmi(weight, height):
    """Вычисляет индекс массы тела с помощью веса и роста пользователя.

    Args:
        weight: Вес пользователя.
        height: Рост пользователя.

    Returns:
        bmi: Индекс массы тела, округленный до 1 знака после запятой.
    """
    return round(weight / (height ** 2), 1)


def calculate_water_needed(weight):
    """Вычисляет количество воды в соответствии с весом пользователя.

    Args:
        weight: Вес пользователя.

    Returns:
        water_litres: Количество воды, необходимое пользователю в литрах.
    """
    # Количество воды, необходимое пользователю, в мл
    water_ml = weight * WATER_PER_KILO
    return water_ml / WATER_ML_PER_LITRE


def output_bmi_and_water_calculation():
    """Выводит на экран отчет для пользователя."""
    user_name, user_age = welcome_user()
    user_weight, user_height = get_user_info()
    user_bmi = calculate_bmi(user_weight, user_height)
    water_litres = calculate_water_needed(user_weight)
    print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)\n"
          f"Твой индекс массы тела: {user_bmi}\n"
          f"Рекомендуемая норма воды: {water_litres:.1f} л в день\n")


output_bmi_and_water_calculation()
print("Расчет окончен. Будьте здоровы!")
