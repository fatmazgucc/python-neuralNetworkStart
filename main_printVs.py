# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf
check_gpu = len ( tf.config.list_physical_devices ( 'GPU'))>0
print (f" Tensor ␣Flow ␣ Ve r si o n : ␣ {tf.__version__}")

print(f" Keras ␣ V e r si o n : ␣ {tensorflow.keras.__version__}" )
print( )
print(f" Python ␣ {sys.version}")
print(f" Pandas ␣ {pd.__version__}")
print (f" S c i k i t −Learn ␣ { sk.__version__}" )
print ( "GPU␣ i s " , " a v a i l a b l e " if check_gpu else "NOT␣AVAILABLE" )