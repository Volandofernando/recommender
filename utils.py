import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_datasets(config):
    df = pd.read_csv("models/processed_dataset.csv")
    return df

def detect_features_and_target(df, config):
    feature_cols = ["moisture_regain","water_absorption","drying_time","thermal_conductivity"]
    target_col = "comfort_score"
    return feature_cols, target_col

def train_model(df, feature_cols, target_col, config):
    X, y = df[feature_cols], df[target_col]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    return model, scaler, X_test, y_test, df

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "r2": round(r2_score(y_test, preds), 3),
        "rmse": round(mean_squared_error(y_test, preds, squared=False), 3)
    }
