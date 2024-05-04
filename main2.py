from main import Student, Person, polishko
from inspect import signature, isfunction

# x = 2
# print(type(x))

# print(type(Student))
print(type(polishko))

personDates = []
# print(personDates)
for attr in dir(polishko):
    if attr.startswith('__') is not True:
        personDates.append(attr)

for item in personDates:
    print(item)

# print('state of attributes')
# for item in personDates:
#     print(hasattr(polishko, item))

print('<--value of attributes-->')
for item in personDates:
    print(type(getattr(polishko, item)))

# personDates2 = signature(Student)
# for item in personDates2.parameters.keys():
#     print(item)
#
# for item in personDates2.parameters.values():
#     print(item)

# polishko.info_all()
# print(isfunction(polishko.info_all()))