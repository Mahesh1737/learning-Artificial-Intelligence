# cnn_cifar10.py
# Requires: tensorflow (>=2.6), matplotlib, numpy
# Run: python cnn_cifar10.py
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks, optimizers
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# 1) Load dataset (CIFAR-10)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
# Normalize images to [0,1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Convert labels to integers (they already are shape (N,1))
y_train = y_train.squeeze()
y_test = y_test.squeeze()
num_classes = 10
input_shape = x_train.shape[1:] # (32, 32, 3)


# 2) Data augmentation (helps generalization)
datagen = ImageDataGenerator(
rotation_range=15,
width_shift_range=0.1,
height_shift_range=0.1,
horizontal_flip=True,
zoom_range=0.05,
fill_mode="reflect"
)

datagen.fit(x_train)


#3) Build a clean, well-regularized CNN
def build_cnn(input_shape, num_classes):
    model = models.Sequential()
    # Block 1
    model.add(layers.Conv2D (32, (3,3), padding="same", input_shape=input_shape))
    model.add(layers. BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers.Conv2D (32, (3,3), padding="same"))
    model.add(layers. BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers. Dropout(0.2))
    
    # Block 2
    model.add(layers.Conv2D (64, (3,3), padding="same"))
    model.add(layers. BatchNormalization())
    model.add(layers.Conv2D (64, (3,3), padding="same"))
    model.add(layers. BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers.Conv2D (64, (3,3), padding="same"))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers. MaxPooling2D((2,2)))
    model.add(layers. Dropout(0.3))
    # Block 3
    model.add(layers.Conv2D(128, (3,3), padding="same"))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers.Conv2D(128, (3,3), padding="same"))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers. Dropout(0.4))
    
    # Classification head
    model.add(layers. Flatten())
    model.add(layers. Dense (256))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation("relu"))
    model.add(layers. Dropout(0.5))
    model.add(layers. Dense (num_classes, activation="softmax"))
    return model
model = build_cnn(input_shape, num_classes)
model.summary()

#4) Compile
learning_rate = 1e-3
opt = optimizers.Adam (learning_rate=learning_rate)
model.compile(optimizer=opt,
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

#5) Callbacks: reduce LR on plateau and early stopping
cb_reduce =  callbacks. ReduceLROnPlateau (monitor="val_loss", factor=0.5, patience=3, verbose=1)
cb_early = callbacks. EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True, verbose=1)
# 6) Train
batch_size = 64
epochs = 50
history = model.fit(
datagen.flow(x_train, y_train, batch_size=batch_size),
steps_per_epoch = len(x_train)//batch_size,
validation_data = (x_test, y_test),
epochs = epochs,
callbacks = [cb_reduce, cb_early],
verbose = 2
I