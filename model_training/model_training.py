import pickle
from sklearn import datasets
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()

#Separate features and target labels.
x=iris.data
y=iris.target

#Split the dataset in train and test sets, later used to get the model accuracy.
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3)

#Build the model using KNeighborsClassifier.
knn=neighbors.KNeighborsClassifier()

#Train the model.
knn.fit(x_train,y_train)

#Do prediction and calculate the accuracy of the model.
predictions=knn.predict(x_test)
print(accuracy_score(y_test,predictions))


#Export the model coefficients in the pickle file. 
with open('model_knn.pkl', 'wb') as model_pkl:
    pickle.dump(knn, model_pkl)