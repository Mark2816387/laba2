print("пример получения/разбиения аргументов – ключевых слов с помощью символа *: ")
def example_args(*args):
    print('Positional argument tuple:', args)
example_args()
example_args(1, 2, 4, 'argument')
