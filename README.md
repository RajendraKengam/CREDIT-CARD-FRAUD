# Flask Fraud Detection API

This is a simple Flask web application that provides a machine learning-powered API for fraud detection. It includes user authentication, prediction history, and an API documentation interface using Swagger.

## Features

*   **User Management**: User signup and login system.
*   **Authentication**: Session-based authentication using Flask-Login.
*   **Fraud Detection**: A `/predict` endpoint that uses a pre-trained Random Forest model to predict fraudulent transactions based on the amount.
*   **Prediction History**: Stores every prediction made by a user in a database.
*   **Database**: Uses SQLite by default, configured with Flask-SQLAlchemy and Flask-Migrate.
*   **API Documentation**: Interactive API documentation available at `/apidocs` via Flasgger (Swagger).
*   **Configuration**: Uses environment variables for configuration.

## Project Structure

```
├── app.py              # Main Flask application
├── models.py           # SQLAlchemy database models
├── train_model.py      # Script to train the ML model
├── test_app.py         # Pytest tests for the application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── index.html
│   ├── login.html
│   └── signup.html
└── model.pkl           # (Generated) Trained ML model
```

## Setup and Installation

Follow these steps to get the application running locally.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required packages using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory by copying the example file.

```bash
copy .env.example .env
```

Then, edit the `.env` file to set your own secret key.

### 5. Train the Machine Learning Model

Run the training script to generate the `model.pkl` file.

```bash
python train_model.py
```

### 6. Run the Application

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Running Tests

To run the automated tests, use `pytest`.

```bash
pytest
```