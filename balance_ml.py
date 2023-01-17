import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


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
    model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=nb_epochs, batch_size=nb_batch)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Loss: {loss}, Accuracy: {accuracy}')
    # Show the plot
    plt.show()

    # Save the model
    model.save('model.h5')

    model_json = model.to_json()

    with open('modele.json', 'w') as f:
        f.write(model_json)


if __name__ == "__main__":
    train()