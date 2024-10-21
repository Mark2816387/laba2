print("пример генератора:")
def my_generate(start=0, stop=10, step=1):
    number = start
    while number <= stop:
        yield number
        number += start
ranger = my_generate(1,9)
for value in ranger:
    print(value)
