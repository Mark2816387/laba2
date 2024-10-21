print("Пример внутренней функции:")
def outer(out_param_1, out_param_2):
    def inner(in_param_1, in_param_2):
        return in_param_1 + in_param_2
    return inner(out_param_1, out_param_2)
print(outer(5,6))
