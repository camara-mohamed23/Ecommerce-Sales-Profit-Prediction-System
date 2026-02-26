def clean_data(df):
    # Supprimer valeurs nulles
    df = df.dropna()

    # Supprimer doublons
    df = df.drop_duplicates()

    # Garder valeurs positives
    df = df[df["Sales"] > 0]
    df = df[df["Quantity"] > 0]

    return df