# -*- coding: utf-8 -*-
from keras.models import load_model
from numpy import array
import numpy as np
from PIL import Image
import sys

img_width, img_height = 150,150
model = load_model('model.h5')

# activate the model
print (sys.argv[1])
img = Image.open(sys.argv[1])
inputData = array(img.resize((img_width,img_height))).reshape(1,img_width,img_height,3)

inputData = np.divide(inputData, 255.0)

print(inputData)

prediction = model.predict(inputData)

print(prediction)
