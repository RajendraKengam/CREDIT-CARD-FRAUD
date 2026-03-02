from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
from models import db, Prediction

app = Flask(__name__)
# A secret key is required for session management
app.secret_key = os.urandom(24)

# --- Database Configuration ---
# Use an absolute path for the database file
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'predictions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# For demonstration, we'll use hardcoded credentials.
# In a real-world application, use a database and hashed passwords.
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == VALID_USERNAME and request.form['password'] == VALID_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not session.get('logged_in'):
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    # Dummy prediction logic: if Amount > 1000, it's fraud.
    # In a real application, you would load and use a trained ML model.
    try:
        amount = float(data.get('Amount', 0))
        if amount > 1000:
            prediction_result = 1  # Fraud
            probability = 0.95
        else:
            prediction_result = 0  # Not Fraud
            probability = 0.15
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid data format for Amount'}), 400

    # Save the prediction to the database
    new_prediction = Prediction(
        payload=str(data),
        prediction=prediction_result,
        fraud_probability=probability
    )
    db.session.add(new_prediction)
    db.session.commit()

    return jsonify({
        'prediction': 'Fraud' if prediction_result == 1 else 'Not Fraud',
        'probability': f'{probability:.2f}'
    })

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)