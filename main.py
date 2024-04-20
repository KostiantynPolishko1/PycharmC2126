# xValue = 10
# xWeight = 5.235
# xName = 'PyCharm'
# flag = True

class Student:
    name: str
    age: int
    group: str

    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def printInfo(self):
        print(f'student: {self.name} - {self.age} - {self.group}')

    def getInfo(self):
        return f'student: {self.name} - {self.age} - {self.group}'


student1 = Student(name='Kostya', age=32, group='C2126')
student1.printInfo()
print(student1.getInfo())

# print(f'student: {student1 .name} - {student1 .age}')
