import shelve
tom = {'pay': 0, 'job': None, 'age': 50, 'name': {'first_name': 'Tom', 'last_name': 'Holland'}}
db = shelve.open('people-shelve')
