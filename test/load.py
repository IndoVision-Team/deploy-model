import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
import numpy as np


model = keras.models.load_model("cnn_model.h5")

# load the image
from PIL import Image
import io
import base64

with open('test/lamp.JPG', "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

base64_decoded = base64.b64decode(encoded_string)
pillow_img = Image.open(io.BytesIO(base64_decoded)).convert('RGB')



# transform image, same as for training!
data = np.asarray(pillow_img)
data = np.expand_dims(data, axis=0)
images = np.vstack([data])
# --> [1, x, y, 1]
images = tf.image.resize(images, [150, 150])


# predict
predictions = model(images)
pred0 = predictions[0]
label0 = np.argmax(pred0)
class_dictionary = {'back_pack': 0, 'bike': 1, 'bike_helmet': 2, 'bookcase': 3, 'bottle': 4, 'calculator': 5, 'desk_chair': 6, 'desk_lamp': 7, 'desktop_computer': 8, 'file_cabinet': 9, 'headphones': 10, 'keyboard': 11, 'laptop_computer': 12, 'letter_tray': 13, 'mobile_phone': 14, 'monitor': 15, 'mouse': 16, 'mug': 17, 'paper_notebook': 18, 'pen': 19, 'phone': 20, 'printer': 21, 'projector': 22, 'punchers': 23, 'ring_binder': 24, 'ruler': 25, 'scissors': 26, 'speaker': 27, 'stapler': 28, 'tape_dispenser': 29, 'trash_can': 30}
key_list = list(class_dictionary.keys())
val_list = list(class_dictionary.values())
position = val_list.index(label0)
print(key_list[position])

