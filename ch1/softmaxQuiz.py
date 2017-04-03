scores = [ 3.0, 1.0, 0.2 ]

import numpy as np

def softmax( x ):
    return np.exp( x ) / np.sum( np.exp( x ), axis = 0 )

import matplotlib.pyplot as plt

x = np.arange( -2.0, 6.0, 0.1 )
scores = np.vstack( [x, np.ones_like( x ), 0.2 * np.ones_like( x )] )

print( scores )
print( softmax(scores ))
print( softmax(scores).T )

plt.plot( x, softmax( scores ).T, linewidth = 2 )
plt.show()
