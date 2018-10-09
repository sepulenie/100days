#03 - тут делаем файл базы данных

import shelve
from Classes_005.classes_PandM import Person
from Classes_005.classes_PandM import Manager

tom = Manager('Tom Doe', 50, 50000)
bob = Person('Bob Toe', 50, 40000, 'hardware')
sue = Person('Sue Taiget', 18, 30000, 'software')

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

