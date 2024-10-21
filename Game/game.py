import random
print("сделал Ягафаров Марк из ПИ-332Б")
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print('Ничья!')
    elif (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 1):
        print('Вы выиграли!')
    else:
        print('Вы проиграли..')

def play_game():
    while True:
        print("\nВыберите 1 - Ножницы, 2 - Бумага, 3 - Камень (или 'exit' для выхода): ")
        
        player_input = input()  # Считывает выбор игрока
        
        if player_input.lower() == 'exit':  # Условие для выхода из игры
            print("Вы вышли из игры.")
            break
        
        if not player_input.isdigit() or int(player_input) not in (1, 2, 3):  # Проверка на ввод некорректных данных
            print('Некорректный ввод! Попробуйте снова.')
            continue
        
        player_choice = int(player_input)  # Преобразуем строку в целое число
        
        # Генерация выбора компьютера (1 - Ножницы, 2 - Бумага, 3 - Камень)
        computer_choice = random.randint(1, 3)
        
        if computer_choice == 1:
            print('Компьютер выбрал ножницы')
        elif computer_choice == 2:
            print('Компьютер выбрал бумагу')
        else:
            print('Компьютер выбрал камень')
        
        # Вызываем функцию для определения победителя
        determine_winner(player_choice, computer_choice)

# Запуск игры
play_game()
