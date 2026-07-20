# Task 4: Noise Analysis and Spatial Filtering

---

## 🔍 Pre-Filter Prediction Hypothesis
* **Hypothesis:** The **Bilateral Filter** is predicted to provide superior high-frequency noise suppression while retaining steep text edge boundaries. Unlike Gaussian or Mean filters which operate uniformly across spatial domains, the Bilateral filter introduces a radiometric intensity component that penalizes kernel smoothing across stark pixel variance thresholds (like dark text on white paper).

---

## 📝 Implementation Summary & Observations
* **Methodology:** Generated a controlled high-frequency noise matrix adhering to a Gaussian distribution ($\mu = 0, \sigma = 25$) and superimposed it onto the single-channel grayscale array of `text_page.jpg`[cite: 1]. The degraded image array was downsampled to 800px width to ensure visual kernel efficacy[cite: 4]. The noisy matrix was then processed through four distinct spatial smoothing frameworks utilizing a steady $7 \times 7$ local neighborhood kernel window: **Mean**, **Gaussian**, **Median**, and **Bilateral**[cite: 4].

* **Engineering Observations:** The empirical results match the edge-preservation hypothesis. The linear smoothing architectures (**Mean** and **Gaussian**) reduce background noise variance effectively, but they completely destroy high-frequency edge gradients, leaving text characters severely blurred and unreadable. The **Median** filter strips out random noise grains well but introduces boxy geometric artifacts on fine text stroke curves. 
  
  The non-linear **Bilateral Filter** delivers the highest quality output for OCR validation; by incorporating an intensity difference weight alongside spatial distance, it smooths out flat paper noise domains while keeping the steep, sharp text edge boundaries beautifully intact.

---

## 🛠️ Resolution Scaling Note
* Processing high-resolution images with standard kernel sizes (e.g., $7 \times 7$) often results in an invisible filtering effect because the kernel operates on a microscopic fraction of the grid. Downsampling the image dimensions or executing a pixel-level zoomed crop is required to bypass screen-scaling limitations and visually verify noise-filtering profiles.