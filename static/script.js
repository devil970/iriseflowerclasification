function showError(msg) {
    const el = document.getElementById('error-message');
    el.textContent = msg;
    el.classList.remove('hidden');
    document.getElementById('result').classList.add('hidden');
}

function clearError() {
    document.getElementById('error-message').classList.add('hidden');
}

async function predictFlower() {
    const sepalLength = document.getElementById('sepal_length').value;
    const sepalWidth = document.getElementById('sepal_width').value;
    const petalLength = document.getElementById('petal_length').value;
    const petalWidth = document.getElementById('petal_width').value;

    if (!sepalLength || !sepalWidth || !petalLength || !petalWidth) {
        showError('Please fill in all fields.');
        return;
    }

    clearError();

    const data = {
        sepal_length: sepalLength,
        sepal_width: sepalWidth,
        petal_length: petalLength,
        petal_width: petalWidth
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.error) {
            showError(result.error);
            return;
        }

        const resultDiv = document.getElementById('result');
        const imageMap = {
            'Iris-setosa': '/static/iris_setosa.png',
            'Iris-versicolor': '/static/iris_versicolor.png',
            'Iris-virginica': '/static/iris_virginica.png'
        };

        document.getElementById('prediction-text').textContent = result.prediction;
        document.getElementById('flower-image').src = imageMap[result.prediction] || '';
        document.getElementById('description-english').textContent = result.description_english;
        document.getElementById('description-hindi').textContent = result.description_hindi;
        resultDiv.classList.remove('hidden');
        resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } catch (error) {
        showError('Error connecting to server: ' + error.message);
    }
}
