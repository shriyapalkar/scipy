from scipy.optimize import  root
from math import sin
def eqn(x):
    return x+sin(x)
myroot=root(eqn,0)
print(myroot.x)