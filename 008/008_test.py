import shelve
import random

db = shelve.open('train_data')
train_set_len = len(db['train_set'][0])
examples = [example for example in db['train_set']]

#Входящая информация
class Input:
    def __init__(self, value):
        self.weight = random.random()
    def change_weight(self, weightToChange):
        self.weight = weightToChange + random.uniform(-0.1,0.1)

class Neuron:
    def __init__(self, input_value, input_weight):

    def activate(self):
        for
        self.neuronValue = input_value * input_weight

class Output:
    def __init__(self,input_value = []):
        self.output =


