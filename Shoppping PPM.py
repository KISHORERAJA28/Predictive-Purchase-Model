import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def load_data(filename):
    
    df = pd.read_csv(filename)

    mo = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'June':5, 
          'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
    
    df['Month'] = df['Month'].map(mo)
    df['VisitorType'] = (df['VisitorType'] == 'Returning_Visitor').astype(int)
    df['Weekend'] = df['Weekend'].astype(int)
    df['Revenue'] = df['Revenue'].astype(int)

        
    X = df.drop('Revenue', axis=1).values.tolist()
    y = df['Revenue'].tolist()

    
