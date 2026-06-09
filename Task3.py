import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential()

model.add(
    LSTM(128, input_shape=(100,1))
)

model.add(Dense(50, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam'
)

print("Music Generation Model Ready")