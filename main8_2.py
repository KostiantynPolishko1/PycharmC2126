def division(a: float, b: float):
    if type(a) == str or type(b) == str:
        return TypeError
    return a / b
