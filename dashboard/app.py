# DASHBOARD FOR BOOKING CANCELLATION PREDICTION

from flask import Flask, render_template, request
import joblib
import numpy as np 
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dataset')
def dataset():
        df = pd.read_csv("data_cleaned.csv")
        return render_template('dataset.html', tables = [df.to_html(
        classes = 'data', header = 'true', justify = 'center')])

@app.route('/visual')
def visual():
    return render_template('visual.html')

# @app.route('/predict', methods = ['POST', 'GET'])
# def predict():
#     if request.method == 'POST':
#         input = request.form

#         return render_template('predict.html', data = input, pred = prediksi)

if __name__ == '__main__':
    model = joblib.load('RandomForestClassifierModel')
    app.run(debug=True)