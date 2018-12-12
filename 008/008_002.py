import shelve
import random

db = shelve.open('train_data')
train_set_len = len(db['train_set'][0])
examples = [example for example in db['train_set']]