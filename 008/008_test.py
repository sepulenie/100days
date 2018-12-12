import numpy as np
import shelve

db = shelve.open('train_data')
train_set = db['train_set']
train_inputs = np.array([i[0] for i in train_set])
train_outputs = np.array([[i[1]] for i in train_set])
print('Train Inputs: \n', train_inputs)
print('Train Outputs: \n', train_outputs)


class Neural_Network(object):
    def __init__(self):
        self.
