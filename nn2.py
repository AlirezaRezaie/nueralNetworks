"""
in nn we need to have a non-zero value for the biases becuase if one nueron outputs 0 the if the bias is 0 too part of the network will become dead and zero 
so we define initial biases non-zero to prevent that issue
----------------------------------------------------------------------------------------------------
the shape of the layer contains of two parameter 
First:
number of input nuerons

Second:
number of next nuerons

overall -> Layer(Inputs,next_nuerons)
"""
import numpy as np


