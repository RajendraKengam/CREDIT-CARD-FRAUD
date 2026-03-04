# Fraud Detection Flask App

This is a robust web application built with Flask for fraud detection. It integrates a Machine Learning model (Random Forest), provides a Swagger API, includes user authentication, and supports Docker deployment.

## Features

- **Machine Learning**:
    - Uses `scikit-learn` to train a Random Forest Classifier.
    - Predicts fraud probability based on transaction amount.
- **API Documentation**:
    - Integrated **Swagger UI** (via Flasgger) to interactively test the API.
- **DevOps & Deployment**:
    - **Dockerized** application with `docker-compose` support.
    - Production-ready server using **Gunicorn**.
- **Backend**:
    - **Flask-Migrate** for database schema management.
    - **Marshmallow** for input validation.
    - **SQLite** database for storing users and prediction history.
- **Authentication**:
    - User Signup/Login with password hashing.
    - Session-based authentication for the dashboard.

## Project Structure

```
.
├── app.py              # Main Flask application logic
├── models.py           # SQLAlchemy database models
├── requirements.txt    # Python dependencies
├── static/             # Static files (CSS, JS)
│   └── login.css
└── templates/          # HTML templates
    ├── index.html
    ├── login.html
    └── signup.html
```

## Setup and Installation

### Prerequisites

- Python 3.x
- `pip` and `venv`

### Installation

1.  **Clone the repository** (or download the source code).
    ```bash
    # git clone <repository-url>
    # cd <repository-folder>
    ```

2.  **Create and activate a virtual environment**:

    - On Windows:
      ```bash
      python -m venv .venv
      .\.venv\Scripts\activate
      ```

    - On macOS and Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

3.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Run the Flask application**:
    ```bash
    python app.py
    ```
    The application will start in debug mode and be accessible at `http://127.0.0.1:5000`.

2.  **Access the application**:
    - Open your web browser and navigate to `http://127.0.0.1:5000`.
    - You will be redirected to the login page.
    - If you don't have an account, click the "Sign Up" link to create one.
    - After signing up, you can log in with your credentials to access the main dashboard.

## How It Works

- **Authentication**: The app uses session-based authentication. After a successful login, the user's ID is stored in the session.
- **Database**: The first time you run the app, a SQLite database file named `predictions.db` will be created in the project directory.
- **Prediction Logic**: The `/predict` endpoint currently contains dummy logic. In a real-world scenario, this is where you would load a trained machine learning model (e.g., from scikit-learn, TensorFlow, or PyTorch) to make predictions based on the input data.