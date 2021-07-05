import tensorflow as tf

shape = (150,150,3)
batch_size = 32
input_shape_batch = (shape[0], shape[1], shape[2])

def get_batch_size():
    return batch_size

def classify(label):
    return "organic or non-recyclable" if label == 0 else "recyclable"

def get_shape():
    return shape

def get_dimension():
    return (shape[0], shape[1])

def train_model(x_train, y_train, x_test, y_test):
    model = tf.keras.Sequential()

    model.add(tf.keras.layers.experimental.preprocessing.Rescaling(1./255, input_shape=input_shape_batch))
    model.add(tf.keras.layers.Conv2D(16, 3, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(4, 4))
    model.add(tf.keras.layers.Dropout(0.2 ))
    model.add(tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(70, activation='relu'))
    model.add(tf.keras.layers.Dense(2))
    model.add(tf.keras.layers.Softmax())

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    
    model.summary()

    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    train_ds = train_ds.batch(batch_size, drop_remainder=True)
    valid_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test))
    valid_ds = valid_ds.batch(batch_size, drop_remainder=True)
    
    history = model.fit(train_ds, epochs=10, batch_size=32, validation_data=valid_ds)

    return model, history