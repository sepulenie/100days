import shelve
import random

db = shelve.open('train_data')
train_set_len = len(db['train_set'][0])
examples = [example for example in db['train_set']]
example = examples[3][0]
desired_result = examples[3][1]
weights = [0.1, 0.4, 0.2]
learning_rate = random.uniform(-0.05,0.05)


def start(inputs=[], weights=[]):
        print('inputs are ',inputs)
        print('weights are ',weights)
        print('Desired Result is ',desired_result)
        current_result = sum([inputs[i]*weights[i] for i in range(0, len(inputs))])
        print('current_result is ', current_result)
        error = abs(current_result - desired_result)
        print('Error is ',error)
        if error > 0.1:
            weights = [w+learning_rate for w in weights]

start(example,weights)