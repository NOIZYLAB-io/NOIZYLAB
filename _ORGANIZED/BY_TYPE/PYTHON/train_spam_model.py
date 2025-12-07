#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Train Spam Detection ML Model
=============================
"""

import pandas as pd
import sqlite3
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np

# Load data
conn = sqlite3.connect("../email-intelligence/email_intelligence.db")
df = pd.read_sql_query("SELECT * FROM email_list", conn)
conn.close()

# Feature engineering
def extract_features(email_data):
    """Extract features from email data"""
    email = email_data.get('email', '')
    domain = email.split('@')[-1] if '@' in email else ''
    text = email_data.get('enriched_info', '{}')
    
    features = [
        len(domain),
        len(email),
        sum(1 for c in email if c.isdigit()),
        1 if domain in ["gmail.com", "yahoo.com", "outlook.com"] else 0,
        sum(1 for c in email if c in "._-"),
        len(domain.split(".")),
        email.count("@"),
        len(text) if isinstance(text, str) else 0
    ]
    
    return features

# Prepare data
X = [extract_features(row) for _, row in df.iterrows()]
y = (df['spam_score'] > 0.7).astype(int).tolist() if 'spam_score' in df.columns else [0] * len(df)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2%}")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "spam_detection_model.pkl")
print("✅ Model saved: spam_detection_model.pkl")

