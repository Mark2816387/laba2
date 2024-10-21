print("пример без замывания, где происходит работа со строкой, когда внутренняя функция добавляет текст в свой аргумент: ")
def outer(out_param):
    def inner(in_param):
        return f 'Outer def have value: {in_param}'
    return inner(out_param)
print(outer('TEST'))
