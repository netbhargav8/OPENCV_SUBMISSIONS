# Task 7: Cross-Perspective Feature Matching via ORB


## 📝 Implementation Summary & Observations

* **Methodology:** 
  1. **Keypoint & Descriptor Extraction:** Extracted rotation- and scale-invariant descriptors across the baseline desk setup (`objects.jpg`) and a secondary alternate-angle capture using an **ORB** feature extractor.
  2. **Descriptor Matching & Ratio Filtering:** Mapped descriptors using a Hamming-distance Brute-Force matcher. Applied **Lowe's Ratio Test** ($0.75$ threshold) on KNN match pairs to discard weak or ambiguous feature vectors.
  3. **Visual Correlation:** Rendered multi-line feature links across frames to evaluate structural alignment and identify which physical items retained the highest descriptor persistence under parallax transformation.

* **Engineering Observations:** Feature matching performance is heavily governed by surface rigidity and gradient uniqueness. High-contrast, structured patterns (such as printed text labels on the marker pens and distinct markings on the watch) maintain consistent binary descriptor signatures even under severe affine and perspective transformations. Conversely, texture-poor regions (such as flat leather panels or plain workspace backdrops) suffer from high descriptor ambiguity, causing the matcher to drop structural links. This demonstrates why feature-based pipelines excel in object recognition and SLAM (Simultaneous Localization and Mapping) only when working with rich, high-gradient surface geometries.