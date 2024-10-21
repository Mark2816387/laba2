from datetime import datetime
print("сделал Ягафаров Марк из ПИ-332Б")
def calculate_age():
    # Получаем сегодняшнюю дату
    today = datetime.today()
    print(f"Сегодняшняя дата: {today.strftime('%d/%m/%Y')}")
    
    # Запрашиваем дату рождения
    birth_date_str = input("Введите дату рождения в формате день,месяц,год: ")

    # Проверяем, чтобы дата состояла только из цифр и запятых
    if not all(char.isdigit() or char == ',' for char in birth_date_str.replace(",", "")):
        print("Ошибка: Дата должна содержать только целые числа и символ ','.")
        return

    try:
        # Разбиваем строку на день, месяц и год
        day, month, year = birth_date_str.split(',')

        # Проверяем, что введены целые числа
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("Ошибка: В дате должны быть только целые числа.")
            return

        # Преобразуем строковые значения в целые числа
        day, month, year = int(day), int(month), int(year)

        # Проверяем, что день, месяц и год не содержат отрицательных значений
        if day <= 0 or month <= 0 or year <= 0:
            print("Ошибка: День, месяц и год должны быть положительными числами.")
            return

        # Создаем объект datetime для даты рождения
        birth_date = datetime(year, month, day)

        # Проверяем, что дата не в будущем
        if birth_date > today:
            print("Ошибка: Дата рождения не может быть в будущем.")
            return

        # Вычисляем возраст
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1  # Уменьшаем возраст, если день рождения еще не наступил в текущем году

        print(f"Ваш возраст: {age} лет.")
    
    except ValueError:
        print("Ошибка: Введите корректную дату в формате день,месяц,год.")

calculate_age()
