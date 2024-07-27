from numpy import *

a=array([[0, 1, 2], [3, 4, 5]])

print("mean:",mean(a,axis=1))
print("standard deviation :",std(a,axis=1))
print("variance :",var(a,axis=1))
