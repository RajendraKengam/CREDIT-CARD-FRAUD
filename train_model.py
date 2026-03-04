import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Generate Synthetic Data
# Features: [Amount]
# Label: 0 (Not Fraud), 1 (Fraud)
print("Generating synthetic data...")
X_normal = np.random.uniform(0, 1000, (1000, 1))
y_normal = np.zeros(1000)

X_fraud = np.random.uniform(800, 5000, (50, 1)) # Fraud tends to be higher amounts
y_fraud = np.ones(50)

X = np.vstack((X_normal, X_fraud))
y = np.concatenate((y_normal, y_fraud))

# 2. Train Model
print("Training Random Forest model...")
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# 3. Save Model
model_path = 'model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(clf, f)
print(f"Model saved to {model_path}")