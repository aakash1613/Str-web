from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
model = pickle.load(open('house.pkl','rb'))


app = Flask(__name__)

@app.route('/',methods = ['GET'])
def main():
    return render_template('index1.html')



@app.route('/predict',methods = ['POST'])
def predict():
  if request.method== 'POST':  
    Area = int(request.form['Area'])
    Bedroom = int(request.form['Bedroom'])
    Bathroom = int(request.form['Bathroom'])
    Stories = int(request.form['Stories'])
    Parking = int(request.form['Parking'])
    FurnishingStatus = int(request.form['FurnishingStatus'])


    prediction= model.predict([[Area,Bedroom,Bathroom,Stories,Parking,FurnishingStatus]])
   
    output=np.round(prediction[0],2)

    if output<0:
        return render_template('index1.html',prediction_text="Sorry you can't purchase house as this combination is not available")
    else:
        return render_template('index1.html',prediction_text="You will cost around INR {}".format(output))
  else :
    return render_template('index1.html') 
    

if __name__ == '__main__':
    app.run(debug=True)