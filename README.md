# Fraud Detection Web Application

This is a full-stack web application built with Flask and Scikit-learn that provides real-time fraud detection for financial transactions. It features a complete user authentication system, a RESTful API for predictions, and a dynamic frontend.

## Key Features

-   **Full User Authentication**: Secure user signup, login, and logout functionality using Flask-Login. Passwords are securely hashed.
-   **ML-Powered Prediction API**: A core `/predict` endpoint that uses a pre-trained Scikit-learn model to classify transactions as fraudulent or not.
-   **Dynamic Frontend**: A responsive, single-page user interface built with Bootstrap and JavaScript that communicates with the backend via AJAX, providing instant feedback without page reloads.
-   **Database Integration**: Uses SQLAlchemy and SQLite to persist user data and a complete history of all predictions made.
-   **Robust Validation**: Employs Marshmallow for server-side validation of API inputs, ensuring data integrity and providing clear error messages.
-   **Comprehensive Testing**: Includes a full test suite using `pytest` to cover authentication, API endpoints, and error handling.
-   **API Documentation**: Integrated Swagger UI for interactive API documentation.
-   **Easy Model Training**: A simple script (`train_model.py`) is provided to generate synthetic data and train the classification model.

## Tech Stack

-   **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Marshmallow
-   **ML**: Scikit-learn, Numpy, Joblib
-   **Frontend**: HTML, Bootstrap 5, JavaScript (Fetch API)
-   **Database**: SQLite
-   **API Docs**: Flasgger (Swagger)
-   **Testing**: Pytest
-   **Deployment**: Gunicorn (recommended)

## Project Structure

```
.
├── templates/
│   ├── index.html
│   ├── login.html
│   └── signup.html
├── .gitignore
├── app.py
├── models.py
├── requirements.txt
├── test_app.py
├── train_model.py
├── .env.example
└── README.md
```

## Setup and Installation

Follow these steps to get the application running locally.

### 1. Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 3. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

-   **Windows (Command Prompt)**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
-   **macOS / Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 4. Install Dependencies

Install all the required Python packages.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory by copying the example file.

```bash
# On Windows (Command Prompt)
copy .env.example .env

# On macOS / Linux
cp .env.example .env
```

Open the `.env` file and change the `SECRET_KEY` to a new, random, and secure string. This is critical for session security.

### 6. Train the Machine Learning Model

Run the training script to generate the `model.pkl` file.

```bash
python train_model.py
```

### 7. Run the Application

You can now start the Flask development server.

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Running Tests

To ensure everything is working as expected, run the test suite:

```bash
pytest
```