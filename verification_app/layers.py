# Custom L1 Distance Layer Module
# Need to load the custom model
import tensorflow as tf
from tensorflow.keras.layers import Layer

# Custom L1 Distance Layer

class L1Dist(Layer):

    def __init__(self,**kwargs):
        super().__init__()

    def call(self,input_embedding,validation_embedding):
        return tf.math.abs(input_embedding-validation_embedding)




