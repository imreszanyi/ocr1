# -*- coding: utf-8 -*-
import os
import random
import numpy as np
from PIL import Image, ImageDraw

number = 0

for dirname, dirnames, filenames in os.walk('training/other'):
    # print path to all filenames.
    print (number)
    for filename in filenames:
        file = os.path.join(dirname, filename)

        # Manipulate
        #for i in range(10):
        img = Image.open(file)
        number+=1
        draw = ImageDraw.Draw(img)
        width, height = img.size
        x1 = random.randint(0, width // 3)
        y1 = random.randint(0, height // 3)
        x2 = random.randint(2 * width // 3, width)
        y2 = random.randint(2 * height // 3, height)
        draw.line((x1,y1, x2,y2), fill=128, width=10)

        #draw.line((0, 0) + img.size, fill=128)
        #draw.line((0, img.size[1], img.size[0], 0), fill=128)


        del draw

        img.save(os.path.join('training/match', str(number) + '.png'))


number = 0

for dirname, dirnames, filenames in os.walk('evaluation/other'):
    # print path to all filenames.
    print (number)
    for filename in filenames:
        file = os.path.join(dirname, filename)

        # Manipulate
        #for i in range(10):
        img = Image.open(file)
        number+=1
        draw = ImageDraw.Draw(img)
        width, height = img.size
        x1 = random.randint(0, width // 3)
        y1 = random.randint(0, height // 3)
        x2 = random.randint(2 * width // 3, width)
        y2 = random.randint(2 * height // 3, height)
        #length = np.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))


        draw.line((x1,y1, x2,y2), fill=128, width=10)

        #draw.line((0, 0) + img.size, fill=128)
        #draw.line((0, img.size[1], img.size[0], 0), fill=128)


        del draw

        img.save(os.path.join('evaluation/match', str(number) + '.png'))


print ("hello")