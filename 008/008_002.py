import shelve
import random

db = shelve.open('train_data')
train_set_len = len(db['train_set'][0])
examples = [example for example in db['train_set']]

#Входящая информация
class Input_neuron:
    def __init__(self, value, inputs_count):
        self.weights = []
        i_c = 0
        while   i_c != inputs_count:
            self.weights.append(random.random())
            i_c += 1
    def changeWeights(self):
        self.changedWeights = []
        for w in self.weights:
            while True:
                c = random.uniform(0.0000000000000010,-0.0000000000000010)
                if w + c < 0 or w + c > 1:
                    pass
                else:
                    self.changedWeights.append(w+c)
                    break
        self.weights=self.changedWeights
        print('__________________________\n')
        print(self.weights)

#Нейрон
class Neuron:
    def __init__(self, input_e, input_weights):
        self.value = [input_e * input_weight for input_weight in input_weights]


'''
def start_training(inputs_count, neuron_count = 0, layer_count = 0):
    layers_array = []
    neurons_array = []
    for each_example in db['train_set']:
        print('Training_Set - ',each_example[0], 'Output - ',each_example[1])

        n = 0
        while n != neuron_count:
            print(round(random.random(), 4))
            n +=1
'''
#start_training(train_set_len, 3, 1)