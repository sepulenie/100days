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
        self.inputSize = len(train_inputs[0])
        self.hiddenSize = 5
        self.outputSize = len(train_outputs[0])
        self.w_fromInput = np.random.randn(self.inputSize, self.hiddenSize)
        self.w_fromHidden = np.random.randn(self.hiddenSize, self.outputSize)

    def forward(self,x):
        self.dotToHiddens = np.dot(x, self.w_fromInput)
        self.activationHidden = self.sigmoid(self.dotToHiddens)
        self.dotToOutput = np.dot(self.activationHidden, self.w_fromHidden)
        activationOutput = self.sigmoid(self.dotToOutput)
        return activationOutput

    def sigmoid(self, s):
        return 1/(1+np.exp(-s))
    def sigmoidPrime(self,s):
        return s * (1 - s)

    def backward(self,train_inputs,train_outputs,activationOutput):
        self.activationOutput_error = train_outputs - activationOutput
        self.activationOutput_error_delta = self.activationOutput_error * self.sigmoidPrime(activationOutput)
        self.z2_error = self.activationOutput_error_delta.dot(self.w_fromHidden.T)
        return self.activationOutput_error, self_z2

nn = Neural_Network()

print('Predicted Output: \n', nn.forward(train_inputs))
print('Error is: \n', nn.backward(train_inputs, train_outputs, nn.forward(train_inputs)))