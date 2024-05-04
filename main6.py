myList = [1, 2, 3, 4, 5]
division = -1
a = 10
b = 3

# if b != 0:
#     division = a / b
#     print(f'{a} / {b} = {division}')
# else:
#     print(f'is not possible divide on {b}')

# try:
#     division = a / b
#     print(f'{a} / {b} = {division}')
# except:
#     print(f'is not possible divide on {b}')

try:
    division = a / b
    print(f'{a} / {b} = {division}')
except (BaseException) as error:
    print(error)
finally:
    myList.append(division)

# except (ZeroDivisionError, TypeError) as error:
#     print(error)
# except (TypeError) as error:
#     print(error)

for value in myList:
    print(value)
