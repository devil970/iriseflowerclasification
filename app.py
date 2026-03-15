from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('models/iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

# Valid ranges derived from the 150-sample Iris dataset
VALID_RANGES = {
    'sepal_length': (4.3, 7.9),
    'sepal_width':  (2.0, 4.4),
    'petal_length': (1.0, 6.9),
    'petal_width':  (0.1, 2.5),
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        parsed = {}
        for field, (low, high) in VALID_RANGES.items():
            try:
                val = float(data[field])
            except (ValueError, TypeError):
                return jsonify({'error': f'{field.replace("_", " ").title()} must be a number.'}), 400
            import math
            if math.isnan(val) or math.isinf(val):
                return jsonify({'error': f'{field.replace("_", " ").title()} is not a valid number.'}), 400
            if not (low <= val <= high):
                return jsonify({'error': f'{field.replace("_", " ").title()} must be between {low} and {high} cm (dataset range).'}), 400
            parsed[field] = val

        features = np.array([[
            parsed['sepal_length'],
            parsed['sepal_width'],
            parsed['petal_length'],
            parsed['petal_width']
        ]])
        
        prediction = model.predict(features)[0]
        
        # Species descriptions
        descriptions = {
            'Iris-setosa': {
                'english': 'Small petals, compact flower. Found in cold regions. Most distinct species.',
                'hindi': 'छोटी पंखुड़ियाँ, सघन फूल। ठंडे क्षेत्रों में पाया जाता है। सबसे अलग प्रजाति।'
            },
            'Iris-versicolor': {
                'english': 'Medium-sized petals, purple-blue color. Found in wetlands and marshes.',
                'hindi': 'मध्यम आकार की पंखुड़ियाँ, बैंगनी-नीला रंग। आर्द्रभूमि में पाया जाता है।'
            },
            'Iris-virginica': {
                'english': 'Large petals, tall flower. Found in coastal areas. Most elegant species.',
                'hindi': 'बड़ी पंखुड़ियाँ, लंबा फूल। तटीय क्षेत्रों में पाया जाता है। सबसे सुंदर प्रजाति।'
            }
        }
        
        return jsonify({
            'prediction': prediction,
            'description_english': descriptions[prediction]['english'],
            'description_hindi': descriptions[prediction]['hindi']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    import os
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
