import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import os
from tensorflow.keras.utils import plot_model
from matplotlib import pyplot as plt

from keras_visualizer import visualizer


def train(nb_epochs, nb_batch):
    # Load the data from the CSV file
    data = pd.read_csv('data.csv')

    # Split the data into features (X) and target (y) variables
    X = data.drop('result', axis=1)
    y = data['result']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Build the model
    model = Sequential()
    model.add(Dense(10, input_dim=X_train.shape[1]))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train, y_train, epochs=nb_epochs, batch_size=nb_batch)
    print(history.history.keys())
    plt.plot(history.history['accuracy'], color='#066b8b')
    plt.plot(history.history['loss'], color='#b39200')
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)

    visualizer(model, format='png', view=True)
    print(f'Loss: {loss}, Accuracy: {accuracy}')
    plot_model(model, to_file="model.png", show_shapes=True, show_layer_names=False, show_layer_activations=True)

    # Show the plot
    plt.show()
    i = 0
    while os.path.exists("result/result%s" % i):
        i += 1
    # Save the model
    model.save("result/result%s/model.h5" % i)

    model_json = model.to_json()

    with open("result/result%s/modele.json" % i, 'w') as f:
        f.write(model_json)


if __name__ == "__main__":
    train()
