# Task 5: Edge Extraction and Topological Contour Counting

---

## 📝 Implementation Summary & Observations

* **Methodology:** 
  1. **Gradient Extraction (Canny):** Processed a cluttered multi-object scene (`objects.jpg`) through a Gaussian blur and a Canny edge detector. Due to low-contrast boundaries between dark objects and the dark wooden table surface, the default thresholds (50, 150) experienced severe edge dropout. Through iterative tuning, the thresholds were adjusted to successfully isolate the major structural borders of the items.
  2. **Topological Mapping:** The binary edge mask was processed using a morphological closing element to fuse fragmented lines. `cv2.findContours` was deployed in `RETR_EXTERNAL` retrieval mode to trace the outermost geometric boundaries of the objects.
  3. **Algorithmic Artifact Rejection:** To prevent the algorithm from counting specular reflections, background table borders, and surface text as independent entities, a spatial area threshold filter was introduced via `cv2.contourArea`. Discontinuous noise loops and marginal boundary artifacts were programmatically purged, aligning the automated output closely with the physical ground truth.

* **Engineering Observations:** Canny edge detection is highly sensitive to localized lighting conditions and background textures. When objects are densely packed or touching, contouring algorithms tend to trace the continuous outer perimeter of the cluster rather than individual items. The implementation demonstrates that combining pre-processing smoothing, tuned gradient thresholds, and mathematical contour pruning (Area Filtering) creates a robust object-counting framework capable of rejecting environmental noise.