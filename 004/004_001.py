#тут мы создаем базу данных
import shelve

bob = {'name': {'first_name': 'Bob', 'last_name': 'Smith'},
       'age': 42,
       'job': {'company': 'Apple inc.', 'job_title': 'janitor'},
       'pay': [10000, 15000]}

sue = {'name': {'first_name': 'Sue', 'last_name': 'Meth'},
       'age': 18,
       'job': {'company': 'Rostelecom', 'job_title': 'manager'},
       'pay': [40000, 45000]}


db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()