# а тут мы меняем внутри базы значения
import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key)
print(db['sue']['name']['first_name'],db['sue']['name']['last_name'])
sue = db['sue']
sue['pay'][0] = 40000
sue['pay'][0] *= 1.5
db['sue'] = sue
for key in db:
    print(key)
db.close()
