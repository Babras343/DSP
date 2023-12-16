import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import asyncio

async def run_AI():

    # Load your dataset
    dataset = pd.read_csv('sensors.csv')  # Update with your actual dataset filename

    # Assume you have a column 'speed' for speed classes and 'rotation' for rotation classes
    x = dataset.drop(columns=["speed", "rotation"])
    y_speed = dataset["speed"]  # Assuming values like 'Slow', 'Fast', 'Stopped'
    y_rotation = dataset["rotation"]  # Assuming values like 'Right', 'Left'

    # Convert categorical labels to numerical labels
    speed_mapping = {'Stopped': 0, 'Slow': 1, 'Fast': 2}
    rotation_mapping = {'Left': 0, 'Right': 1}

    y_speed = y_speed.map(speed_mapping)
    y_rotation = y_rotation.map(rotation_mapping)

    # Split the data into a training set and a testing set for speed detection
    x_train, x_test, y_speed_train, y_speed_test = train_test_split(x, y_speed, test_size=0.2)

    # Build and train the model for speed detection
    speed_model = tf.keras.models.Sequential()
    speed_model.add(tf.keras.layers.Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))
    speed_model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
    speed_model.add(tf.keras.layers.Dense(3, activation='softmax'))  # 3 classes for speed
    speed_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    speed_model.fit(x_train, y_speed_train, epochs=1000)

    # Evaluate the speed detection model
    speed_model.evaluate(x_test, y_speed_test)

    # Split the data into a training set and a testing set for rotation detection
    x_train, x_test, y_rotation_train, y_rotation_test = train_test_split(x, y_rotation, test_size=0.2)

    # Build and train the model for rotation detection
    rotation_model = tf.keras.models.Sequential()
    rotation_model.add(tf.keras.layers.Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))
    rotation_model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
    rotation_model.add(tf.keras.layers.Dense(2, activation='softmax'))  # 2 classes for rotation
    rotation_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    rotation_model.fit(x_train, y_rotation_train, epochs=1000)

    # Evaluate the rotation detection model
    rotation_model.evaluate(x_test, y_rotation_test)

asyncio.run(run_AI())
