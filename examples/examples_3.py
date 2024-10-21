print("Пример функции с одним аргументом:")
def example(color):
    if color == "dark":
        return "This is tree"
    elif color == "blue":
        return "This is sky"
    else:
        return "I don't know"
what_is_it = example('blue')
print(what_is_it)

