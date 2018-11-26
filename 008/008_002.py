import shelve
import random
db = shelve.open('train_data')

def start_training(inputs_count, neurons = 0):
    print(inputs_count)
    weights = []
    while inputs_count > 0:
        weights.append(random.random())
        inputs_count -= 1
    print(weights)




start_training(len(db['train_set'][1]), 3)