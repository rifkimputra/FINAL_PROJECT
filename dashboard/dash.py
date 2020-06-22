from flask import Flask, render_template, request
from data import data_clean
from prediction import prediction

app=Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/data')
def data():
    data = data_clean()
    return render_template ('data.html', data=data)

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/prediction',methods= ['GET','POST'])
def prediction_html():
    if request.method == 'POST':
        data = request.form
        data=data.to_dict()
        data['deposit_type']=int(data['deposit_type'])
        data['lead_time']=float(data['lead_time'])
        data['country']=int(data['country'])
        data['price']=float(data['price'])
        data['total_of_special_requests']=int(data['total_of_special_requests'])
        data['arrival_date_day_of_month']=int(data['arrival_date_day_of_month'])
        data['arrival_date_week_number']=int(data['arrival_date_week_number'])
        data['market_segment']=int(data['market_segment'])
        data['previous_cancellations']=int(data['previous_cancellations'])

        result = prediction(data)
        return render_template('result.html', hasil_prediksi=result)
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True,port=2000)