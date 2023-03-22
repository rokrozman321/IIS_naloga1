from flask import Flask, request, jsonify
import pandas as pd
import pickle
import os

import joblib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({"status": "OK"})

@app.route('/air/predict/', methods=['POST'])
def predict():
    data = request.get_json() # pridobimo json file
    df = pd.DataFrame.from_dict([data]) # shranimo json file v df
    print(df)
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'models', 'model2.joblib')
    loaded_model = joblib.load(model_path)  
    # napovemo vrednost
    predictions = loaded_model.predict(df)
    # # vrnemo vrednost
    return jsonify({"predict": float(predictions)})
    # return jsonify({df})

def run_app():
    app.run(host='0.0.0.0', port=5000)

# run_app()