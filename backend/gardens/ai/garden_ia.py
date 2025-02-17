import tensorflow as tf
import numpy as np

class GardenAI:
    def __init__(self):
        self.model = tf.keras.models.load_model('gardens/ai/plant_detection.h5')
        self.classes = ['róża', 'tulipan', 'drzewo_iglaste', 'trawa']

    def analyze_image(self, img_path):
        img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        predictions = self.model.predict(img_array)
        return [self.classes[i] for i, prob in enumerate(predictions[0]) if prob > 0.7]
