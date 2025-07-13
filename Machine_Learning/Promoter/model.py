import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

def model(input_file="merged_features.csv"):
    df = pd.read_csv(input_file)
    X = df.drop(columns=["gene_id", "promoter_sequence", "activity"])
    y = df["activity"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_temp, X_test, y_temp, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)
    model = XGBRegressor()
    model.fit(X_train, y_train)
    val_preds = model.predict(X_val)
    test_preds = model.predict(X_test)
    print(f"Validation R2: {r2_score(y_val, val_preds):.4f}")
    print(f"Test R2: {r2_score(y_test, test_preds):.4f}")
    print(f"MSE: {mean_squared_error(y_test, test_preds):.4f}")
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, test_preds, color='blue', alpha=0.5)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
    plt.xlabel("Actual Activity")
    plt.ylabel("Predicted Activity")
    plt.title("Actual vs Predicted Promoter Activity")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("promoter_prediction_plot.png")
    plt.show()
