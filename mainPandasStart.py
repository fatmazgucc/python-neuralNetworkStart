# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pandas as pd
import numpy as np
from sklearn import metrics
from scipy.stats import zscore

def remove_outliers ( df , name , sd ) :
    drop_rows = df.index[(np.abs(df[name].mean() - df[name])>=(sd * df[name].std()))]
    df.drop ( drop_rows , axis =0, inplace=True )


df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", na_values =['NA','?'])
print(df[0:5])
print("Yeyyy i readed any csv for the first time. Let's continue :)")


# create feature vector
print("taking median of horsepower column")
med = df['horsepower'].median ( )
df['horsepower']=df['horsepower'].fillna(med)
print("ggg")
# Drop the name column
df.drop('name', 1 , inplace=True )
# Drop outliers in horsepoer
print ( "Length ␣ before ␣MPG␣ outliers ␣dropped : ␣ {} " . format (len (df) ) )
remove_outliers(df , 'mpg' , 2 )
print ( " Length ␣ a f t e r ␣MPG␣ o u t l i e r s ␣ dropped : ␣ {} " . format (len ( df ) ) )
pd.set_option ( 'display.max_columns' , 0 )
pd.set_option ( 'display.max_rows' , 5 )
print(df)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/