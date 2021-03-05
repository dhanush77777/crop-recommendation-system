from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('crop.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index5.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    
    
    
    if prediction=='rice':
        return render_template('index5.html', prediction_text='you probably have to grow rice in your field')
    elif prediction=='maize':
        return render_template('index5.html', prediction_text='you probably have to grow maize in your field')
    elif prediction=='chickpea':
        return render_template('index5.html', prediction_text='you probably have to grow chickpea in your field')
    elif prediction=='kidneybeans':
        return render_template('index5.html', prediction_text='you probably have to grow kidneybeans in your field')
    elif prediction=='pigeonpeas':
        return render_template('index5.html', prediction_text='you probably have to grow pigeonpeas in your field')
    elif prediction=='mothbeans':
        return render_template('index5.html', prediction_text='you probably have to grow mothbeans in your field')
    elif prediction=='mothbeans':
        return render_template('index5.html', prediction_text='you probably have to grow mothbeans in your field')
    elif prediction=='blackgram':
        return render_template('index5.html', prediction_text='you probably have to grow blackgram in your field')
    elif prediction=='lentil':
        return render_template('index5.html', prediction_text='you probably have to grow lentil in your field')
    elif prediction=='pomegranate':
        return render_template('index5.html', prediction_text='you probably have to grow pomegranate in your field')
    elif prediction=='banana':
        return render_template('index5.html', prediction_text='you probably have to grow banana in your field')
    elif prediction=='mango':
        return render_template('index5.html', prediction_text='you probably have to grow mango in your field')
    elif prediction=='grapes':
        return render_template('index5.html', prediction_text='you probably have to grow grapes in your field')
    elif prediction=='watermelon':
        return render_template('index5.html', prediction_text='you probably have to grow watermelon in your field')
    elif prediction=='muskmelon':
        return render_template('index5.html', prediction_text='you probably have to grow muskmelon in your field')
    elif prediction=='apple':
        return render_template('index5.html', prediction_text='you probably have to grow apple in your field')
    elif prediction=='orange':
        return render_template('index5.html', prediction_text='you probably have to grow orange in your field')
    elif prediction=='papaya':
        return render_template('index5.html', prediction_text='you probably have to grow papaya in your field')
    elif prediction=='coconut':
        return render_template('index5.html', prediction_text='you probably have to grow coconut in your field')
    elif prediction=='cotton':
        return render_template('index5.html', prediction_text='you probably have to grow cotton in your field')
    elif prediction=='jute':
        return render_template('index5.html', prediction_text='you probably have to grow jute in your field')
    else:
        return render_template('index5.html', prediction_text='you probably have to grow coffee in your field')
        
      
      
   
      
    
 
    
 
        

    
 


if __name__ == '__main__':
    app.run(debug=True)
