# Fraud Detection Flask App

This is a simple web application built with Flask that provides a template for a fraud detection service. It includes user authentication, a dashboard to view prediction history, and an API endpoint for making predictions.

## Features

- **User Management**:
    - User signup with name, email, and password.
    - User login and logout.
    - Session management to protect routes.
- **Database**:
    - Uses SQLite to store user and prediction data.
    - Models for `User` and `Prediction` are defined using Flask-SQLAlchemy.
- **Prediction**:
    - A `/predict` API endpoint to submit data for fraud detection.
    - Saves prediction requests and results to the database, linked to the user.
- **Frontend**:
    - Simple HTML templates for login, signup, and a main dashboard.
    - The dashboard displays the logged-in user's name and a history of their predictions.

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