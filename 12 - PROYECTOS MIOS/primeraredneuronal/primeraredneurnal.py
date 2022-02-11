#Primero importamos las librerias con las que vamos a trabajar.
import tensorflow as tf
import numpy as np

# Definimos los valores de entrada
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit= np.array ([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimezers.Adam(0.001),
    loss='mean_squeared_error'
)

print ("Comenzando entrenamiento....")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=false)
print ("Modelo Entrenado")