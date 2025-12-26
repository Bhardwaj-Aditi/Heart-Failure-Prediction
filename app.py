from flask import Flask, render_template, request
import pickle as pkl

app = Flask(__name__)

# Load trained model
model = pkl.load(open('heart_model.pkl', 'rb'))

# FIXED feature order (MUST match training data)
FEATURE_ORDER = [
    'age',
    'anaemia',
    'creatinine_phosphokinase',
    'diabetes',
    'ejection_fraction',
    'high_blood_pressure',
    'platelets',
    'serum_creatinine',
    'serum_sodium',
    'sex',
    'smoking'
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs in correct order
        features = []
        for field in FEATURE_ORDER:
            value = float(request.form.get(field))
            features.append(value)

        # Basic input validation (important medical sanity checks)
        age = features[0]
        ejection_fraction = features[4]
        serum_creatinine = features[7]

        if age <= 0 or age > 120:
            return render_template('result.html', result="Invalid age entered.")

        if ejection_fraction <= 0 or ejection_fraction > 100:
            return render_template('result.html', result="Invalid ejection fraction value.")

        if serum_creatinine <= 0:
            return render_template('result.html', result="Invalid serum creatinine value.")

        # Prediction
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1]
        risk_percent = round(probability * 100, 2)

        # Risk interpretation
        if risk_percent >= 70:
            risk_level = "High Risk of Heart Failure"
        elif risk_percent >= 40:
            risk_level = "Moderate Risk of Heart Failure"
        else:
            risk_level = "Low Risk of Heart Failure"

        result = f"{risk_level} ({risk_percent}%)"

        return render_template('result.html', result=result)

    except Exception as e:
     return render_template(
        'result.html',
        result=f"ERROR: {e}"
    )


if __name__ == '__main__':
    app.run(debug=True)
