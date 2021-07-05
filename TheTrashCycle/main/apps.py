from django.apps import AppConfig
import os
import tensorflow as tf

class MainConfig(AppConfig):
    name = 'main'
    type_model = tf.keras.models.load_model('main/models/type-classifier3')
