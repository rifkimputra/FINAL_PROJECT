  
import joblib
from pandas import DataFrame

model = joblib.load('modelJoblib')

def prediction(data):
    df= DataFrame(data,index=[0])
    result = model.predict(df)
    hasil_prediksi=[]
    if result == 1:
        hasil_prediksi.append('is likely to be cancelled')
    else:
        hasil_prediksi.append('is likely to be succeded')
    return hasil_prediksi[0]