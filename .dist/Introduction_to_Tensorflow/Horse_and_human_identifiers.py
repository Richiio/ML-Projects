from tensorflow import keras 
model = features = tf.layers.max_pooling2d(
    features, pool_size=2, strides=2, padding="same")