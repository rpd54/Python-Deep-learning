from sklearn import datasets, metrics
from scipy import sparse
from sklearn.cross_validation import train_test_split
#Choose one of the dataset using the datasets features in the scikit-learn
from sklearn import svm
from sklearn.datasets import load_boston,load_digits
import numpy as np
#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning)

C = 1.0
#getting the data and response of the dataset
#choosing
digits=load_digits() #load dataset
x=digits.data
y=digits.target
#According to your dataset, split the data to 20% testing data, 80% training data(you can also use any other number)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#Apply SVC with Linear kernel
model = svm.SVC(kernel='linear')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy for SVC linear kernel " + str(metrics.accuracy_score(y_test,y_pred)))
#Apply SVC with RBF kernel
model = svm.SVC(kernel='rbf')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy for SVC with rbf kernel " + str(metrics.accuracy_score(y_test,y_pred)))