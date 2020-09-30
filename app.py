import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = []
    a , b, c, d, e, f = [x for x in request.form.values()]
    int_features.append(b)
    int_features.append(c)
    int_features.append(d)
    int_features.append(e)
    int_features.append(f)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output == 0:
        output = "Fail"
    else:
        output = "Pass"
    return render_template('index.html', prediction_text='Result : {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    output = label_encoder.inverse_transform(output)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)