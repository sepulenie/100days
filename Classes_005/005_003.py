import shelve

db=shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
tom = db['tom']
print(bob.name)
print(db['tom'].lastName())

