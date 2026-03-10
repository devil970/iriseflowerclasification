# 🌸 Iris Flower Classification System

A web-based Machine Learning project that predicts the species of Iris flowers using a trained Random Forest model.

## 📁 Project Structure

```
Red Queen/
│
├── iris/                      # Dataset folder
│   ├── iris.data             # Iris dataset
│   └── bezdekIris.data
│
├── models/                    # Trained ML models
│   └── iris_model.pkl        # Saved model (generated after training)
│
├── static/                    # Frontend assets
│   ├── style.css             # CSS styling
│   └── script.js             # JavaScript logic
│
├── templates/                 # HTML templates
│   └── index.html            # Main web interface
│
├── train_model.py            # ML model training script
├── app.py                    # Flask backend server
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🚀 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Dataset**: Iris Dataset

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🔧 Installation Steps

1. **Clone or download the project**

2. **Navigate to the project directory**
   ```bash
   cd "Red Queen"
   ```

3. **Install required Python libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Machine Learning model**
   ```bash
   python train_model.py
   ```
   This will create `iris_model.pkl` in the `models/` folder.

5. **Run the Flask application**
   ```bash
   python app.py
   ```

6. **Open your web browser and visit**
   ```
   http://127.0.0.1:5000
   ```

## 💡 How to Use

1. Enter the following measurements in centimeters:
   - **Sepal Length** (e.g., 5.1)
   - **Sepal Width** (e.g., 3.5)
   - **Petal Length** (e.g., 1.4)
   - **Petal Width** (e.g., 0.2)

2. Click the **"Predict Species"** button

3. View the prediction result:
   - **Iris-setosa**
   - **Iris-versicolor**
   - **Iris-virginica**

## 📊 Sample Test Data

| Sepal Length | Sepal Width | Petal Length | Petal Width | Expected Species |
|--------------|-------------|--------------|-------------|------------------|
| 5.1          | 3.5         | 1.4          | 0.2         | Iris-setosa      |
| 6.7          | 3.0         | 5.2          | 2.3         | Iris-virginica   |
| 5.7          | 2.8         | 4.1          | 1.3         | Iris-versicolor  |

## 🎓 Project Features

✅ Clean and modern web interface  
✅ Real-time prediction using trained ML model  
✅ Random Forest Classifier with high accuracy  
✅ Responsive design  
✅ Easy to use and demonstrate  

## 📝 Notes

- The model achieves approximately **95-100% accuracy** on the test set
- The Random Forest algorithm is used for robust predictions
- All input values should be in centimeters

## 👨‍💻 Author

College Project - Iris Flower Classification System

## 📄 License

This project is open source and available for educational purposes.
