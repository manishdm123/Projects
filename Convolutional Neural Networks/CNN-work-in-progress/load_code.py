# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:26:43 2017

@author: abc12
"""

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import numpy as np

os.chdir("C:/Users/abc12/Desktop/Cats Dogs dataset");

#model.save("first_try.h5")
test_model=load_model("Test.h5")

img_width,img_height = im.size
for i in range(1,40):
    str1 = 'test1/' +str(i)+'.jpg'
    img=load_img(str1,False,target_size=(150,150))


#img=load_img('test1/1.jpg')
    x=img_to_array(img)
    x=np.expand_dims(x,axis=0)
    
    preds=test_model.predict_classes(x)
    
    prob=test_model.predict_proba(x)
    print(preds,prob)
    str2= str(preds)
    
    if (int(str2[2]) == 1):
        img.save('dogs/'+str(i)+'.jpg')
    else:
        img.save('cats/'+str(i)+'.jpg')
            
        
