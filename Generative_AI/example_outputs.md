# Example Outputs

# Template 1 — Basic Prediction Explainer

## Test Case 1

### Input
- Height: 160 cm
- Hips: 36 inches
- Category: Dress
- Size Ordered: S
- Prediction: Small

### Generated Output
The system predicted that this item may run small for the selected size. The dress may feel tighter than expected.

---

## Test Case 2

### Input
- Height: 170 cm
- Hips: 40 inches
- Category: Dress
- Size Ordered: M
- Prediction: Fit

### Generated Output
The selected item is likely to fit the customer comfortably based on the provided measurements.

---

## Test Case 3

### Input
- Height: 175 cm
- Hips: 44 inches
- Category: Dress
- Size Ordered: L
- Prediction: Large

### Generated Output
The system predicted that this item may run large for the selected size and may feel loose.

---

# Template 2 — Personalized Measurement-Based Advice

## Test Case 1

### Input
- Height: 160 cm
- Hips: 36 inches
- Category: Dress
- Size Ordered: S
- Prediction: Small

### Generated Output
Based on the customer’s measurements, the selected size S may feel slightly tight around the hips and waist. Trying one size larger may improve comfort.

---

## Test Case 2

### Input
- Height: 170 cm
- Hips: 40 inches
- Category: Dress
- Size Ordered: M
- Prediction: Fit

### Generated Output
The selected size M appears suitable for the customer’s body proportions and preferred dress style.

---

## Test Case 3

### Input
- Height: 175 cm
- Hips: 44 inches
- Category: Dress
- Size Ordered: L
- Prediction: Large

### Generated Output
The selected size may provide a loose fit depending on the dress design and fabric style.

---

# Template 3 — Cluster-Aware Recommendation

## Test Case 1

### Input
- Cluster: Petite/Tight-Fit Group
- Prediction: Small

### Generated Output
This customer belongs to a cluster that frequently experiences tight-fitting dresses. The selected item may feel restrictive.

---

## Test Case 2

### Input
- Cluster: Balanced-Fit Group
- Prediction: Fit

### Generated Output
Customers in this cluster usually experience accurate sizing. The selected dress is expected to fit comfortably.

---

## Test Case 3

### Input
- Cluster: Tall/Loose-Fit Group
- Prediction: Large

### Generated Output
This customer belongs to a cluster that often experiences loose-fitting items. The dress may appear oversized.

---

# Template 4 — Actionable Shopping Recommendation

## Test Case 1

### Input
- Height: 160 cm
- Hips: 36 inches
- Category: Dress
- Prediction: Small

### Generated Output
The selected dress may run small for this customer profile. Trying size M may provide a more comfortable fit.

---

## Test Case 2

### Input
- Height: 170 cm
- Hips: 40 inches
- Category: Dress
- Prediction: Fit

### Generated Output
The selected size is expected to fit well. No size adjustment is currently recommended.

---

## Test Case 3

### Input
- Height: 175 cm
- Hips: 44 inches
- Category: Dress
- Prediction: Large

### Generated Output
The selected item may feel oversized. Customers who prefer a tighter fit may consider trying a smaller size.