#Тут мы забиваем базу для тренировки
import shelve

train_set = [[[0,0,1],0],
             [[1,1,1],1],
             [[1,0,1],1],
             [[0,1,1],0]
             ]

db = shelve.open('train_data')
db['train_set'] = train_set
db.close()