import random
print("сделал Ягафаров Марк из ПИ-332Б")
def find_multiples():
    while True:
        # Генерация списка случайных чисел в диапазоне от 0 до 200
        random_numbers = [random.randint(0, 200) for _ in range(10)]
        print(f"Сгенерированный список чисел: {random_numbers}")
        
        # Защита от некорректного ввода
        try:
            # Запрашиваем у пользователя число X или команду выхода
            x = input("Введите число X, кратные которому нужно найти (или 'exit' для выхода): ")
            
            if x.lower() == 'exit':
                print("Выход из программы.")
                break  # Выход из цикла

            # Проверяем, что введено целое положительное число
            if not x.isdigit() or int(x) <= 0:
                print("Ошибка: Введите целое положительное число.")
                continue  # Возвращаемся к следующему запросу
            
            # Преобразуем X в целое число
            x = int(x)
            
            # Используем лямбда-функцию для фильтрации кратных чисел
            multiples = list(filter(lambda num: num % x == 0, random_numbers))
            
            # Выводим результаты
            if multiples:
                print(f"Числа, кратные {x}: {multiples}")
            else:
                print(f"Нет чисел, кратных {x}.")
        
        except ValueError:
            print("Ошибка: Введите корректное число.")

# Запуск функции с циклом
find_multiples()
