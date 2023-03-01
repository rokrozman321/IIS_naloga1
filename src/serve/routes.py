from flask import jsonify, request, Blueprint
import os
import joblib
import pandas as pd

main = Blueprint("main", __name__)

@main.route('/', methods=['GET'])
def test():
    return jsonify({"status": "OK"})

@main.route('/air/predict/', methods=['POST'])
def predict():
    
    data = request.get_json() # pridobimo json file
    df = pd.DataFrame.from_dict([data]) # shranimo json file v df
    print(df)
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'models', 'model1.joblib')
    loaded_model = joblib.load(model_path)  
    # # napovemo vrednost
    predictions = loaded_model.predict(df)

    # # vrnemo vrednost
    return jsonify({"predict": float(predictions)})