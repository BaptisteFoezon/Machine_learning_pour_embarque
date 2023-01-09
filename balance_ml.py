import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, plot_confusion_matrix
from sklearn.model_selection import train_test_split


class estimator:
  _estimator_type = ''
  classes_=[]
  def __init__(self, model, classes):
    self.model = model
    self._estimator_type = 'classifier'
    self.classes_ = classes
  def predict(self, X):
    y_prob= self.model.predict(X)
    y_pred = y_prob.argmax(axis=1)
    return y_pred

# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Split the data into features (X) and target (y) variables
X = data.drop('result', axis=1)
y = data['result']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build the model
model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')
classifier = estimator(model, ["Balance", "No Balance"])
figsize = (12,12)
plot_confusion_matrix(estimator=classifier, X=X_test, y_true=y_test, cmap='Blues', normalize='true', ax=plt.subplots(figsize=figsize)[1])
# Show the plot
plt.show()

# Save the model
model.save('model.h5')

model_json = model.to_json()

with open('modele.json', 'w') as f:
    f.write(model_json)

