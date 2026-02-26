from data_loader import load_data
from data_cleaning import clean_data
from feature_engineering import engineer_features
from train_model import train_model
from evaluate import evaluate_model


def main():
    # 1. Chargement des données
    df = load_data("ecommerce.csv")

    # 2. Nettoyage
    df = clean_data(df)

    # 3. Feature Engineering
    df = engineer_features(df)

    # 4. Entraînement modèle
    model, X_test, y_test = train_model(df)

    # 5. Évaluation
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()