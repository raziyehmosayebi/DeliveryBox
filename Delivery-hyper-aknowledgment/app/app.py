from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np
import os

app = Flask(__name__)

model_path = os.getenv('MODEL_PATH', 'best_model.json')  

model = xgb.XGBClassifier()
model.load_model(model_path)  

@app.route('/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400
    
    data = request.get_json()
    
    expected_keys = ["deliverey_category_id", "weekday", "time_bucket", 
                     "total_distance", "sum_product", "final_customer_fare", 
                     "source_hexagonID", "destination_hexagonID"]
    
    if not all(key in data for key in expected_keys):
        return jsonify({"error": "JSON is missing one or more required keys"}), 400
    
    features = np.array([[data[key] for key in expected_keys]])
    
    prediction = model.predict(features)
    
    return jsonify({"prediction":prediction.tolist() })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
