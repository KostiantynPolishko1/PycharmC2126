def arihmeticOperation(symbol: str):
    typeOperation = symbol

    def operation(a: int, b: int) -> float:
        if typeOperation == '+':
            return a + b
        else:
            return f'operation \"{typeOperation}\" has not realization'

    return operation


sumNumbers = arihmeticOperation('-')
value1 = 2
value2 = 5

result = sumNumbers(value1, value2)
print(result)