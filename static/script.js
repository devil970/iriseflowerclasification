const FIELD_LABELS = {
    sepal_length: 'sepal_length',
    sepal_width:  'sepal_width',
    petal_length: 'petal_length',
    petal_width:  'petal_width'
};

function showError(msg) {
    const el = document.getElementById('error-message');
    el.innerHTML = `
        <div class="error-icon">&#9888;</div>
        <div class="error-body">
            <span class="error-title">Invalid Input</span>
            <span class="error-detail">${msg}</span>
        </div>
        <button class="error-close" onclick="clearError()">&times;</button>
    `;
    el.classList.remove('hidden');
    el.classList.add('error-animate');
    document.getElementById('result').classList.add('hidden');

    // Highlight the offending field
    Object.keys(FIELD_LABELS).forEach(id => {
        const input = document.getElementById(id);
        const label = input.closest('.input-group').querySelector('label');
        const fieldName = id.replace('_', ' ');
        if (msg.toLowerCase().includes(fieldName)) {
            input.classList.add('input-error');
            label.classList.add('label-error');
        } else {
            input.classList.remove('input-error');
            label.classList.remove('label-error');
        }
    });
}

function clearError() {
    const el = document.getElementById('error-message');
    el.classList.add('hidden');
    el.classList.remove('error-animate');
    document.querySelectorAll('.input-error').forEach(i => i.classList.remove('input-error'));
    document.querySelectorAll('.label-error').forEach(l => l.classList.remove('label-error'));
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
