from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the saved model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])

            # Create input with 30 features: 28 zeros, Time = 0, and given amount
            input_data = np.array([[0]*28 + [0, amount]])  # Shape (1, 30)

            # Scale input using saved scaler
            input_data_scaled = scaler.transform(input_data)

            # Predict
            result = model.predict(input_data_scaled)
            prediction = "✅ Transaction is LEGITIMATE" if result[0] == 0 else "❌ Transaction is FRAUDULENT"
        except:
            prediction = "⚠️ Invalid input. Please enter a valid amount."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
