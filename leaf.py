#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/Thato Kenny Sefoloko/Downloads/Compressed/Plant-Leaf-Disease-Prediction-main/Plant-Leaf-Disease-Prediction-main/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_limela(limela_plant):
  test_image = load_img(limela_plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict plants or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==0:
      return "BOLOUKOMO BO BOTSÓ", 'BOLOUKOMO.html'
       
  elif pred==1:
      return "HLOENYA", 'HLOENYA.html'
        
  elif pred==3:
      return "LEKHALA LA QUTHING", 'QUTHING.html'
        
  elif pred==4:
      return "LELEME LA KHOMO", 'KHOMO.html'
       
  elif pred==5:
      return "LELETA LA PHOFU", 'PHOFU.html'
        
  elif pred==6:
      return "LEMATLA", 'LEMATLA.html'
        
  elif pred==7:
      return "LESOKO", 'LESOKO.html'
        
  elif pred==8:
      return "MAKHOLELA", 'MAKHOLELA.html'
  elif pred==9:
      return "SEHOLOBE", 'SEHOLOBE.html'
        
  elif pred==2:
      return "KHOMO EA BALISA", 'BALISA.html'

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('C:/Users/Thato Kenny Sefoloko/Downloads/Compressed/Plant-Leaf-Disease-Prediction-main/Plant-Leaf-Disease-Prediction-main/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_limela(limela_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
