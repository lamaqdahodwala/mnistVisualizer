# from tensorflow import keras
# import tensorflow as tf
from keras.utils import to_categorical
from keras import models
from keras import layers
from keras.datasets import mnist

train_data, test_data = mnist.load_data()

x_train, y_train = train_data
x_test, y_test = test_data

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = (x_train >= 0.5).astype(int)
x_test = (x_test >= 0.5).astype(int)

x_train = x_train.reshape((60000, 784))
x_test = x_test.reshape((10000, 784))

network = models.Sequential()
network.add(layers.Dense(128, activation='relu', input_shape=(784,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy']) 

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

network.fit(x_train, y_train, epochs=5, batch_size=128)

network.evaluate(x_test, y_test, 128)
network.save('my_model.keras')


