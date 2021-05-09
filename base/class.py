# Person类定义
class Person:
    def __init__(self,age):
        self.age = age
    def info(self):
        print('my age: %d' % self.age)

# Student子类继承父类Person
class Student(Person):
    def __init__(self,age,grade):
        self.grade = grade
        #调用父类的构函
        Person.__init__(self,age)
    def info(self):
        print('我今年%d, 上%d年级了' % (self.age, self.grade))

if __name__ == '__main__':
    stu = Student(20, 1)
    stu.info()