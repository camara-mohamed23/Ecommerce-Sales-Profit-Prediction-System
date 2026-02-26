import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib


def train_model(df):
    X = df[["Quantity", "Year", "Month", "Revenue_per_Unit"]]
    y = df["Profit"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Création automatique du dossier models
    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/trained_model.pkl")

    return model, X_test, y_test