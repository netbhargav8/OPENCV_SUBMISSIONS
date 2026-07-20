# Task 6: Thresholding and Morphological Filtering


## 📝 Implementation Summary & Observations

* **Methodology:** 
  1. **Binarization (Otsu's Method):** Converted the grayscale array of `text_page.jpg` into a crisp binary map. Otsu's algorithm automatically calculated the optimal threshold boundary by analyzing the bimodal histogram distribution of the paper background versus dark text ink.
  2. **Morphological Closing:** To repair broken character strokes and remove internal pixel voids, a morphological closing filter (`cv2.morphologyEx` with `MORPH_CLOSE`) was applied using a structured rectangular kernel.
  3. **Comparative Word Cropping:** Extracted identical bounding box arrays before and after closing to visually evaluate stroke continuity.

* **Engineering Observations:** Morphological operations are strictly dependent on kernel-to-font scale ratios. A `3x3` kernel provides the precise footprint needed to resolve sub-millimeter pinholes in text vectors at an 800px image scale. Scaling the kernel up carelessly causes severe typographic bleeding, fusing distinct words together and destroying structural readability, which would heavily degrade downstream OCR (Optical Character Recognition) parsing accuracy.