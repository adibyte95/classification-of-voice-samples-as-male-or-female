# here we will do the actual coding to train our model and test it
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
# step 1 first we need to convert male and female label as 0 and 1

data_path = "data.csv"
df = pd.read_csv(data_path)

df['label'].replace('female',0, inplace = True)
df['label'].replace('male',1, inplace = True)

# dividing the available data into train data and test data 
mydata_train, mydata_test = train_test_split(df, random_state=0, test_size=.2)
# for pre processing the data because If a feature has a variance that is orders of magnitude larger that others
#it might dominate the objective function and make the estimator unable to learn from other features correctly as expected

scaler = StandardScaler()
# we are using only the first 20 columns as features and the 21 column i.e label column as label
scaler.fit(mydata_train.ix[:,0:20])
X_train = scaler.transform(mydata_train.ix[:,0:20])
X_test = scaler.transform(mydata_test.ix[:,0:20])
y_train = list(mydata_train['label'].values)
y_test = list(mydata_test['label'].values)

# we will use a number of classifier 

# K nearest neighbour classifier
print('using KNN classifier we will have :')
clf = KNeighborsClassifier(n_neighbors=4) 
model = clf.fit(X_train, y_train) 
print('accuracy on training set : ',clf.score(X_train,y_train))
print('accuracy on testing set : ',clf.score(X_test,y_test))


# using support vector machines 
print('using support vector machines : ')
SVM = SVC().fit(X_train , y_train)
print('accuracy on training set : ',SVM.score(X_train,y_train))
print('accuracy on testing set : ',SVM.score(X_test,y_test))

# using multi layered perceptron
print('multi layered perceptron')
mlp = MLPClassifier(random_state=0).fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(mlp.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(mlp.score(X_test, y_test)))

