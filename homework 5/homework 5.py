print("сделал Ягафаров Марк из ПИ-332Б")
def get_number():
    for number in range(1,30,2): #генерация от 1 до 29 с шагом 2 для нечётных значений
        yield number
numbers = get_number()
lst = list(numbers)
first = lst[0]
fifth = lst[4]
last = lst[-1]
print('Первое, пятое и последнее значения: ', first, ', ', fifth, ', ', last)
