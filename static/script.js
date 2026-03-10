async function predictFlower() {
    const sepalLength = document.getElementById('sepal_length').value;
    const sepalWidth = document.getElementById('sepal_width').value;
    const petalLength = document.getElementById('petal_length').value;
    const petalWidth = document.getElementById('petal_width').value;
    
    if (!sepalLength || !sepalWidth || !petalLength || !petalWidth) {
        alert('Please fill in all fields');
        return;
    }
    
    const data = {
        sepal_length: sepalLength,
        sepal_width: sepalWidth,
        petal_length: petalLength,
        petal_width: petalWidth
    };
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.error) {
            alert('Error: ' + result.error);
            return;
        }
        
        const resultDiv = document.getElementById('result');
        const predictionText = document.getElementById('prediction-text');
        const flowerImage = document.getElementById('flower-image');
        const descEnglish = document.getElementById('description-english');
        const descHindi = document.getElementById('description-hindi');
        
        // Map species to image
        const imageMap = {
            'Iris-setosa': '/static/iris_setosa.png',
            'Iris-versicolor': '/static/iris_versicolor.png',
            'Iris-virginica': '/static/iris_virginica.png'
        };
        
        predictionText.textContent = result.prediction;
        flowerImage.src = imageMap[result.prediction] || '';
        descEnglish.textContent = result.description_english;
        descHindi.textContent = result.description_hindi;
        resultDiv.classList.remove('hidden');
        
        resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } catch (error) {
        alert('Error connecting to server: ' + error.message);
    }
}
