#01 - тут просто тестируем всю хрень
from Classes_005.classes_PandM import Person

rick = Person('Rick Ronson', 23, 3000, 'janitor')
dick = Person('Richard Bronson', 80, 500, 'pensioner')
rick.giveRaise(1)
print(int(rick.pay))