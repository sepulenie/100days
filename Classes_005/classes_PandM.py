#01 - тут делаем классы

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, persent):
        self.pay *= (1.0 + persent)
    def __str__(self):
        return ('<%s => %s: %s, %s>' %
                (self.__class__.__name__, self.name, self.job, self.pay))


class Manager(Person):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay, __class__.__name__)
    def giveRaise(self, persent, bonus=0.1):
        Person.giveRaise(self,persent+bonus)