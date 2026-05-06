# =============================================================
# predict.py
# Load the saved models and get a clothing fit prediction.
# Accepts RAW (unscaled) user measurements — scaling and cluster
# assignment are handled automatically.
## =============================================================

import joblib
import numpy as np
import pandas as pd
import json

# ------------------------------------------------------------------
# 1. Load models 
# ------------------------------------------------------------------
model           = joblib.load("Supervised_Learning/model/rf_model.joblib")
scaler          = joblib.load("Supervised_Learning/model/scaler.joblib")
kmeans          = joblib.load("Supervised_Learning/model/kmeans_model.joblib")
kmeans_features = joblib.load("Supervised_Learning/model/kmeans_features.joblib")

# ------------------------------------------------------------------
# 2. Collect raw input from the user
# ------------------------------------------------------------------
print("=" * 50)
print("  Clothing Fit Predictor")
print("=" * 50)

print("\nClothing category options:")
categories = ['bottoms', 'dresses', 'new', 'outerwear', 'sale', 'tops', 'wedding']
for i, cat in enumerate(categories, 1):
    print(f"  {i}. {cat}")

cat_choice = int(input("Enter category number: ")) - 1
cat_flags = [0] * 7
cat_flags[cat_choice] = 1

print("\nEnter measurements (raw values, no need to scale):")
size     = float(input("  Size (e.g. 10, 12, 14 ...): "))
quality  = float(input("  Quality rating (1-5): "))
cup_size = float(input("  Cup size (numeric, e.g. A=1, B=2, C=3, D=4 ...): "))
hips     = float(input("  Hips (cm or inches, same unit as training data): "))
bra_size = float(input("  Bra size (e.g. 34, 36, 38 ...): "))
height   = float(input("  Height (cm or inches, same unit as training data): "))
length   = float(input("  Length preference (1=petite to 5=tall): "))

# ------------------------------------------------------------------
# 3. Scale the numerical inputs
# ------------------------------------------------------------------
raw_num_cols = ['size', 'quality', 'cup size', 'hips', 'bra size', 'height', 'length']
raw_nums_df  = pd.DataFrame([[size, quality, cup_size, hips, bra_size, height, length]],
                             columns=raw_num_cols)
scaled_nums = scaler.transform(raw_nums_df)[0]

# Map scaled values back to named dict for easy lookup
scaled_map = {
    'size_scaled':       scaled_nums[0],
    'quality_scaled':    scaled_nums[1],
    'cup size_scaled':   scaled_nums[2],
    'hips_scaled':       scaled_nums[3],
    'bra size_scaled':   scaled_nums[4],
    'height_scaled':     scaled_nums[5],
    'length_scaled':     scaled_nums[6],
}

# Map cat flags to named dict
cat_map = {
    'cat_bottoms':   cat_flags[0],
    'cat_dresses':   cat_flags[1],
    'cat_new':       cat_flags[2],
    'cat_outerwear': cat_flags[3],
    'cat_sale':      cat_flags[4],
    'cat_tops':      cat_flags[5],
    'cat_wedding':   cat_flags[6],
}

# ------------------------------------------------------------------
# 4. Build RF feature vector 
# ------------------------------------------------------------------
rf_feature_names = [
    'cat_bottoms', 'cat_dresses', 'cat_new', 'cat_outerwear',
    'cat_sale', 'cat_tops', 'cat_wedding',
    'size_scaled', 'quality_scaled', 'cup size_scaled',
    'hips_scaled', 'bra size_scaled', 'height_scaled', 'length_scaled'
]
all_values = {**cat_map, **scaled_map}
rf_vector = pd.DataFrame([[all_values[f] for f in rf_feature_names]], columns=rf_feature_names)

# ------------------------------------------------------------------
# 5. Predict fit label (Random Forest)
# ------------------------------------------------------------------
label_map     = {0: "fit", 1: "small", 2: "large"}
raw_pred      = model.predict(rf_vector)[0]
probabilities = model.predict_proba(rf_vector)[0]
class_labels  = model.classes_

prediction = label_map.get(int(raw_pred), str(raw_pred))

print("\n" + "=" * 50)
print(f"  Predicted Fit: {prediction.upper()}")
print("=" * 50)
print("\nConfidence per class:")
for raw_label, prob in zip(class_labels, probabilities):
    label = label_map.get(int(raw_label), str(raw_label))
    bar   = "█" * int(prob * 30)
    print(f"  {label:<8}  {prob:.1%}  {bar}")

# ------------------------------------------------------------------
# 6. Build KMeans vector 
# ------------------------------------------------------------------
kmeans_vector = pd.DataFrame(
    [[all_values[f] for f in kmeans_features]],
    columns=kmeans_features
)
cluster_id = int(kmeans.predict(kmeans_vector)[0])

cluster_descriptions = {
    0: "customers with balanced body measurements and average length preference, mostly associated with new-category items",
    1: "customers with slightly higher size, bra size, and cup size, mostly associated with tops",
    2: "customers with lower size and shorter clothing length, mostly associated with dresses",
    3: "customers with longer clothing length and balanced measurements, mostly associated with bottoms",
    4: "customers with higher quality scores and compact body measurements, mostly associated with outerwear",
    5: "customers with mixed preferences and smaller group size, mostly associated with sale or wedding items"
}

cluster_description = cluster_descriptions[cluster_id]
print(f"\n  Cluster: {cluster_id} — {cluster_description}")

# ------------------------------------------------------------------
# 7. Build result dict
# ------------------------------------------------------------------
result = {
    "prediction":          prediction,               # T1, T2, T3, T4
    "height":              height,                   # T2, T4
    "hips":                hips,                     # T2, T4
    "bra_size":            int(bra_size),            # T2, T4
    "cup_size":            int(cup_size),            # T2, T4
    "length":              length,                   # T2, T4
    "size":                size,                     # T2, T4
    "quality":             quality,                  # T4
    "category":            categories[cat_choice],   # T4
    "cluster_description": cluster_description,      # T3
}

print("\nResult dict (pass this to our Llama prompt builder):")
print(json.dumps(result, indent=2))