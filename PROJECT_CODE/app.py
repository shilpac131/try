import collect
import pickle
import time
import serial
import numpy as np
from time import sleep
from flask import Flask, request, render_template

model = pickle.load(open('/home/sc/codes/model1.pkl', 'rb'))
app = Flask(__name__)
app.add_url_rule('/photos/<path:filename>', endpoint='photos', view_func=app.send_static_file)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dekho', methods=['POST'])
def dekho():

    while True:

        final_features = [np.array(collect.seethis())]
        prediction = model.predict(final_features)
        output = (prediction[0])
        return render_template('index.html', prediction_text='The soil is {} and soil moisture is {}'.format(output,final_features[0][0]))


if __name__ == "__main__":
    app.run(debug=True)
