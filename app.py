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

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([[
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
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
    app.run(debug=True)
