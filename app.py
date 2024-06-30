from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import math

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ai')
def index_func():
    return render_template("ai.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_input=[float(x) for x in request.form.values()]
    input_data=[np.array(int_input)]
    print(input_data)
    prediction=model.predict(input_data)
    conf = model.predict_proba(input_data)
    a = conf[0][prediction[0]]*100
    confidence = round(a, 2)
    print(confidence)
    print(prediction[0])
    output='{0:.{1}f}'.format(prediction[0], 2)

    if prediction[0] == 1:
        return render_template('ai.html',pred='The given sample is safe for aquatic life', confidence1 = 'Confidence is {}'.format(confidence) + '%', cval = confidence, cval1 = '{} %'.format(confidence))
    else:
        return render_template('ai.html', pred='The given sample is not safe for aquatic life', confidence1 = 'Confidence is {}'.format(confidence) + '%', cval = confidence, cval1 = '{} %'.format(confidence))


if __name__ == '__main__':
    app.run(debug=True)