import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/Thato Kenny Sefoloko/Downloads/Compressed/Plant-Leaf-Disease-Prediction-main/Plant-Leaf-Disease-Prediction-main/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

tomato_plant = cv2.imread('C:/Users/Thato Kenny Sefoloko/Downloads/Compressed/Plant-Leaf-Disease-Prediction-main/Plant-Leaf-Disease-Prediction-main/Dataset/test/L.jpg')
test_image = cv2.resize(tomato_plant, (128,128)) # load image 
  
test_image = img_to_array(test_image)/255 # convert image to np array and normalize
test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
result = model.predict(test_image) # predict diseased palnt or not
  
pred = np.argmax(result, axis=1)
print(pred)
if pred==0:
    print("BOLOUKOMO BO BOTSÓ")
       
elif pred==1:
    print("HLOENYA")
        
elif pred==3:
    print("LEKHALA LA QUTHING")
        
elif pred==4:
    print("LELEME LA KHOMO")
       
elif pred==5:
    print("LELETA LA PHOFU")
        
elif pred==2:
    print("KHOMO EA BALISA")
        
elif pred==6:
    print("LEMATLA")
        
elif pred==7:
      print("LESOKO")
elif pred==8:
      print("MAKHOLELA")
        
elif pred==9:
      print("SEHOLOBE")
