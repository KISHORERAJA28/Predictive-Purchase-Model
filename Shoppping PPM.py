import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def load_data(filename):
        
    X = df.drop('Revenue', axis=1).values.tolist()
    y = df['Revenue'].tolist()
    
    return X, y

def evaluate(actual, predicted):
    
    tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
    tn = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 0)
    
    pos = sum(actual)
    neg = len(actual) - pos
    

    sens, spec = evaluate(y_test, preds)
    
    print(f"Correct: {(y_test == preds).sum()}")
    print(f"Incorrect: {(y_test != preds).sum()}")
    print(f"Sensitivity: {100 * sens:.2f}%")
    print(f"Specificity: {100 * spec:.2f}%")

if __name__ == "__main__":
    main()
