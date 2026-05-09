# Cluster Interpretation & Profiles (K-Means, k = 6)

**Overall:**

Final cluster assignments used for the system come from K-Means (k = 6); DBSCAN was run for comparison/outliers on a sample and is not used. Clusters were created using scaled body/fit features (e.g., size, hips, height, bra size, cup size, length, quality) plus item category indicators (bottoms, dresses, new, outerwear, sale, tops, wedding). Each cluster represents a distinct *fit + shopping-category* segment.

### Cluster 0 (n ≈ 21,488) — Balanced measurements + "New" shoppers
- **Key traits:** balanced/average measurements and moderate length preference
- **Dominant category:** `cat_new`
- **Interpretation:** mainstream users; general fit guidance works well, and "new arrivals" recommendations are most relevant

### Cluster 1 (n ≈ 20,364) — Tops-focused + slightly larger bust sizing
- **Key traits:** slightly higher size, bra size, cup size (relative to others)
- **Dominant category:** `cat_tops`
- **Interpretation:** users where upper-body fit matters more; advice should emphasize bust, comfort, structure, and sizing for tops

### Cluster 2 (n ≈ 18,650) — Dresses-focused + smaller size + shorter length
- **Key traits:** relatively lower size and shorter length preference
- **Dominant category:** `cat_dresses`
- **Interpretation:** dress shoppers who benefit from guidance on dress length/fit (e.g., shorter hemlines, petite-friendly options)

### Cluster 3 (n ≈ 15,266) — Bottoms-focused + longer length preference
- **Key traits:** longer length preference with otherwise balanced measurements
- **Dominant category:** `cat_bottoms`
- **Interpretation:** bottoms-first segment; advice should highlight inseam/length fit and hip/waist fit

### Cluster 4 (n ≈ 4,223) — Outerwear-focused + quality-oriented niche
- **Key traits:** higher quality score with compact measurements
- **Dominant category:** `cat_outerwear`
- **Interpretation:** smaller segment that values quality; recommend outerwear emphasizing material, durability, and layering fit

### Cluster 5 (n ≈ 2,799) — Sale-driven + occasional wedding items (mixed niche)
- **Key traits:** mixed preferences; smallest cluster suggests niche behavior
- **Dominant category:** mostly `cat_sale` with some `cat_wedding`
- **Interpretation:** value seekers and/or special-occasion shoppers; advice should focus on budget, value, and event suitability
