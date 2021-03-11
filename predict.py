from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from settings import *
import numpy as np


mdoel = load_model(MODEL_PATH)

def predict_class(img_path):
    img = image.load_img(img_path, target_size=(150, 150))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    pred_class = int(mdoel.predict(x) > 0.5)
    if pred_class == 0:
        class_name = 'cat'
    else:
        class_name = 'dog'
    return class_name
