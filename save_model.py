# Run this ONCE to persist the trained models to disk, and they will be ignored "not pushed due there relatively big size"

import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

os.makedirs("Supervised_Learning/model", exist_ok=True)

# ------------------------------------------------------------------
# 1. Load the preprocessed dataset
# ------------------------------------------------------------------
df = pd.read_csv("Dataset/preprocessed_data.csv")
df_model = df.drop(['review_summary', 'review_text'], axis=1)

# ------------------------------------------------------------------
# 2. Fit the scaler on raw numerical columns
# ------------------------------------------------------------------
raw_num_cols = ['size', 'quality', 'cup size', 'hips', 'bra size', 'height', 'length']
scaler = StandardScaler()
scaler.fit(df_model[raw_num_cols])

# ------------------------------------------------------------------
# 3. Assemble the feature matrix for the Random Forest
# ------------------------------------------------------------------
rf_features = [
    'cat_bottoms', 'cat_dresses', 'cat_new', 'cat_outerwear',
    'cat_sale', 'cat_tops', 'cat_wedding',
    'size_scaled', 'quality_scaled', 'cup size_scaled',
    'hips_scaled', 'bra size_scaled', 'height_scaled', 'length_scaled'
]

X = df_model[rf_features]
y = df_model['fit']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------------
# 4. Train Random Forest (best hyperparameters from GridSearchCV)
# ------------------------------------------------------------------
best_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=1,
    class_weight=None,
    random_state=42,
    n_jobs=-1
)
best_rf.fit(X_train, y_train)
print("Random Forest trained successfully.")

# ------------------------------------------------------------------
# 5. Train KMeans 
# ------------------------------------------------------------------
scaled_cols   = [col for col in df.columns if col.endswith('_scaled')]
category_cols = [col for col in df.columns if col.startswith('cat_')]
kmeans_features = scaled_cols + category_cols

X_cluster = df[kmeans_features].copy()
X_cluster = X_cluster.fillna(X_cluster.median())

kmeans_final = KMeans(n_clusters=6, random_state=42, n_init=10)
kmeans_final.fit(X_cluster)
print("KMeans trained successfully.")
print("KMeans feature order:", kmeans_features)

# ------------------------------------------------------------------
# 6. Save everything
# ------------------------------------------------------------------
joblib.dump(best_rf,        "Supervised_Learning/model/rf_model.joblib")
joblib.dump(scaler,         "Supervised_Learning/model/scaler.joblib")
joblib.dump(kmeans_final,   "Supervised_Learning/model/kmeans_model.joblib")
joblib.dump(kmeans_features,"Supervised_Learning/model/kmeans_features.joblib")

print("Saved: rf_model.joblib")
print("Saved: scaler.joblib")
print("Saved: kmeans_model.joblib")
print("Saved: kmeans_features.joblib")
print("\nDone! You can now use predict.py without re-training.")