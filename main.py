# xValue = 10
# xWeight = 5.235
# xName = 'PyCharm'
# flag = True

class Student:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student(name='Kostya', age=32)
print(f'student: {student1 .name} - {student1 .age}')
