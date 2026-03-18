import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def load_data(filename):
    
    df = pd.read_csv(filename)

    
    mo = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'June':5, 
          'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
    
    df['Month'] = df['Month'].
    
    
    df['VisitorType'] = (df['VisitorType'] == 'Returning_Visitor').astype(int)
    df['Weekend'] = df['Weekend'].astype(int)
    df['Revenue'] = df['Revenue'].astype(int)
    
    
    X = df.drop('Revenue', axis=1).values.tolist()
    y = df['Revenue'].tolist()
    
    return X, y

def evaluate(actual, predicted):
    
    tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
    tn = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 0)
    
    pos = sum(actual)
    neg = len(actual) - pos
    
    return (tp / pos, tn / neg)

def main():
    if len(sys.argv) != 2:
        print("Provide the data file!")
        return

   
    X, y = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    
    sens, spec = evaluate(y_test, preds)
    
    print(f"Correct: {(y_test == preds).sum()}")
    print(f"Incorrect: {(y_test != preds).sum()}")
    print(f"Sensitivity: {100 * sens:.2f}%")
    print(f"Specificity: {100 * spec:.2f}%")

if __name__ == "__main__":
    main()
