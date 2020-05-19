import numpy as np

def roll(boost :int = 0, sides :int= 20):
    return np.random.randint(1,sides+1) + boost
