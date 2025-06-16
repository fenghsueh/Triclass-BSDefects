# Tri-classified Ball Screw Defect Dataset

This three-class ball screw surface defect dataset is a modified version of the bi-classified dataset originally published by the Karlsruhe Institute of Technology. It introduces a refined labeling to more accurately represent the real-world conditions of the test samples.

![demo](demo.png)

## Dataset Structure

The dataset consists of RGB images (150×150 pixels) representing different surface conditions of ball screws. The images are categorized into the following classes:

- `pitting` (label: 3) — 10,760 samples  
- `contaminated` (label: 6) — 7,523 samples  
- `normal` (label: 8 — 3,552 samples  

The contaminated class consists of re-labeled samples from the original `normal` category that exhibited clear signs of lubricant contamination.

## Directory Layout

``KIT-BS-recls/``

``├── labels.txt        # Label file with {sample_path}{space}{integer_label} format``

``├── samples/``

``│   ├── contaminated/ # Lubricant-contaminated samples``

``│   ├── normal/       # Normal surface samples``

``│   └── pitting/      # Pitting defect samples``



## How to Use

1. Clone this repository.
2. Use `KIT-BS-recls/samples` for reclassified images in three class groups. Each image is a 150x150 RGB `.png` file.
3. Use `labels.txt` for supervised learning setups; it maps each image file directory to its class label.

## License

This dataset is distributed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/), in accordance with the license of the original dataset.  

## Note on Modifications

This dataset was adapted by relabeling a subset of the `normal` class samples to form a new category: `contaminated`. This reflects samples affected by lubricant presence and improves the clarity of the classification task.

## Citation Requirements

If you use this dataset or find it helpful, please consider citing the original work and referencing this repository:

1. Original paper: 
   - Schlagenhauf, Tobias (2023): Ball Screw Drive Surface Defect Dataset for Classification. Karlsruhe Institute of Technology. DOI: 10.35097/1511

2. This repository & related paper: 
   - Feng Xue, Weimin Zhang, Shulian Xie, Alexander Puchta, Jürgen Fleischer. Domain-unique group- and its subgroup-aware diagnostics for ball screw surface defects: An open set domain adaptation approach. https://github.com/fenghsueh/Triclass-BSDefects (Under review)
   - *The final citation format will be formally settled once the related paper is published online.*


## Access to Original Dataset

The original two-class dataset can be obtained from:
https://publikationen.bibliothek.kit.edu/1000133819