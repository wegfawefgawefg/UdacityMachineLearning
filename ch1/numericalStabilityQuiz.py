start = 1
tiny = 0.000001

summation = start
for i in range( 0, 1000000 ):
    summation = summation + tiny

summation = summation - start

print( summation )
