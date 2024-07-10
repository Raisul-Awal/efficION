#Adopted from Tensorflow/Keras. Set to preference 


def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(100, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='gelu'),
      layers.Dense(64, activation='gelu'),
      layers.Dense(64, activation='LeakyReLU'),
      layers.Dense(64, activation='LeakyReLU'),
      layers.Dense(30, activation='gelu'),
      layers.Dense(30, activation='gelu'),
      layers.Dense(10, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='mean_absolute_error',
                  metrics=['accuracy'],
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

dnn_model = build_and_compile_model(normalizer)
dnn_model.summary()
