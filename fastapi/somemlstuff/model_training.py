import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load processed dataset
df = pd.read_csv("processed_features.csv")

# Separate features and labels
X = df.drop(columns=["label"])  # Features
y = df["label"]  # Target labels

# Normalize features (important for distance-based models)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")


model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Detailed report
print(classification_report(y_test, y_pred))

joblib.dump(model, "logistic_regression_model.pkl")
joblib.dump(scaler, "scaler.pkl") 