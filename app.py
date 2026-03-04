from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
from models import db, Prediction, User
from flask_migrate import Migrate
from flasgger import Swagger
from marshmallow import Schema, fields, ValidationError, EXCLUDE
from dotenv import load_dotenv
import joblib
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

load_dotenv()

app = Flask(__name__)
# A secret key is required for session management
app.secret_key = os.getenv('SECRET_KEY', 'default_dev_secret')

# --- Database Configuration ---
# Use an absolute path for the database file
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'predictions.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
swagger = Swagger(app)

# --- Flask-Login Configuration ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# --- Load ML Model ---
model = None
try:
    model = joblib.load(os.path.join(basedir, 'model.pkl'))
except FileNotFoundError:
    print("Warning: model.pkl not found. Predictions will use dummy logic.")

# --- Input Validation Schema ---
class PredictionInputSchema(Schema):
    Amount = fields.Float(required=True, validate=lambda x: x > 0)

    class Meta:
        # Ignore unknown fields in the input
        unknown = EXCLUDE

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        # Fetch user by name
        user = User.query.filter_by(name=name).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        if User.query.filter((User.email == email) | (User.name == name)).first():
            error = 'Name or Email address already exists.'
            return render_template('signup.html', error=error)

        # Create new user
        new_user = User(
            name=name,
            email=email
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html', error=error)

@app.route('/')
@login_required
def index():
    # current_user is available automatically
    predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.timestamp.desc()).all()
    
    return render_template('index.html', user=current_user, predictions=predictions)

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    """
    Fraud Detection Endpoint
    ---
    tags:
      - Prediction
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            Amount:
              type: number
              example: 1500.50
    responses:
      200:
        description: Successful prediction
      400:
        description: Invalid input
      401:
        description: Unauthorized
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    # Validate input
    try:
        schema = PredictionInputSchema()
        validated_data = schema.load(data)
        amount = validated_data['Amount']
    except ValidationError as err:
        # Flatten Marshmallow's error dictionary for a user-friendly message
        error_message = ". ".join([f"{field}: {', '.join(messages)}" for field, messages in err.messages.items()])
        return jsonify({'error': error_message}), 400

    # Prediction logic
    if model:
        # Reshape for sklearn: [[amount]]
        features = [[amount]]
        prediction_result = int(model.predict(features)[0])
        
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(features)[0][1]
        else:
            probability = 0.95 if prediction_result == 1 else 0.10
    else:
        # Fallback dummy logic
        if amount > 1000:
            prediction_result = 1
            probability = 0.95
        else:
            prediction_result = 0  # Not Fraud
            probability = 0.15

    # Save the prediction to the database
    new_prediction = Prediction(
        payload=str(data),
        prediction=prediction_result,
        fraud_probability=probability,
        user_id=current_user.id
    )
    db.session.add(new_prediction)
    db.session.commit()

    return jsonify({
        'prediction': 'Fraud' if prediction_result == 1 else 'Not Fraud',
        'probability': f'{probability:.2f}'
    })

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)