import numpy as np
import matplotlib.pyplot as plt

def softmax( x ):
    return np.exp( x ) / np.sum( np.exp( x ), axis = 0 )

def crossEntropy( labels, probabilities ):
    return -1 * np.sum( labels * np.log( probabilities ) )

scores = np.array( [3.0, 1.0, 0.2] )
print( scores )
print( softmax( scores ) )
print( softmax( scores / 10.0 ) )
