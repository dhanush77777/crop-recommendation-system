from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import sqlite3
import json

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
    result = prediction[0]

    con = sqlite3.connect('test.db',isolation_level=None)
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE foobar (nitrogen INTEGER, phosphorus INTEGER, potassium INTEGER, temperature INTEGER, humidity INTEGER, ph_level INTEGER, rainfall INTEGER)")
    except Exception as e:
        print(e)
    cur.executemany("INSERT INTO foobar VALUES (?,?,?,?,?,?,?)", final_features)
    con.commit()
    
    return render_template('index5.html', prediction_text=f'you probably have to grow {result} in your field')
    


if __name__ == '__main__':
    app.run(debug=True)
