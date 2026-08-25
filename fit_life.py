# Проект FitLife - MVP версия 1.0
def welcome_user():
    """Returns name and age of application user"""
    print("Приветсвуем вас в нашем приложении FitLife!")
    user_name = input("Введите ваше имя: ").title()
    print(f"Привет, {user_name}!")
    user_age = int(input("Введите ваш возраст в годах (например, 23): "))
    return user_name, user_age


def get_user_info():
    """Returns weight and height of an application user"""
    user_weight = float(input("Введите ваш вес в кг (56 или 56.2): "))
    user_height = float(input("Введите ваш рост в метрах (например, 1.7): "))
    return user_weight, user_height


def calculate_bmi(weight, height):
    """Returns body mass index calculated from weight and height"""
    # Расчет индекса массы тела
    return round(weight / (height ** 2), 1)


def calculate_water_needed(weight):
    """Returns an amount of water is needed for a person per day in litres"""
    # количество воды, необходимое на 1 кг веса человека, в мл
    WATER_NEED_PER_KILO = 30
    # количество воды, необходимое пользователю, в мл
    water_ml = weight * WATER_NEED_PER_KILO
    # количество воды, необходимое пользователю, в л
    return water_ml / 1000


def output_bmi_and_water_calculation():
    """Print report for user"""
    user_name, user_age = welcome_user()
    user_weight, user_height = get_user_info()
    user_bmi = calculate_bmi(user_weight, user_height)
    water_litres = calculate_water_needed(user_weight)
    print()
    print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
    print(f"Твой индекс массы тела: {user_bmi}")
    print(f"Рекомендуемая норма воды: {water_litres:.1f} л в день")
    print()


output_bmi_and_water_calculation()
print("Расчет окончен. Будьте здоровы!")
