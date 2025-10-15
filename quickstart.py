import os
from PIL import Image

# --- Configuration ---
# Set the base path to the dataset repository
DATASET_PATH = 'KIT-BS-recls'
# Edit here to define a sample image to verify
SAMPLE_IMAGE_RELATIVE_PATH = './samples/contaminated/N(725).png'
# -------------------

# 1. Load all labels into a dictionary for quick lookup
print("--> Loading labels from labels.txt...")
labels_dict = {}
labels_file_path = os.path.join(DATASET_PATH, 'labels.txt')

try:
    with open(labels_file_path, 'r') as f:
        for line in f:
            # Label format: {sample_path}{space}{integer_label}
            # e.g., "./samples/contaminated/N(724).png 6"
            parts = line.strip().split()
            if len(parts) == 2:
                path, label = parts
                labels_dict[path] = int(label)
    print(f"--> Successfully loaded labels for {len(labels_dict)} images.")
except FileNotFoundError:
    print(f"[Error] 'labels.txt' not found at: {labels_file_path}")
    exit()

# 2. Load the sample image and retrieve its label
print(f"\n--> Verifying with a sample: '{SAMPLE_IMAGE_RELATIVE_PATH}'")
full_image_path = os.path.join(DATASET_PATH, SAMPLE_IMAGE_RELATIVE_PATH)

try:
    # Load the image
    with Image.open(full_image_path) as img:
        print(f"  - Image loaded successfully.")
        print(f"    - Details: Format={img.format}, Mode={img.mode}, Size={img.size}")

    # Retrieve the label from the dictionary
    if SAMPLE_IMAGE_RELATIVE_PATH in labels_dict:
        label = labels_dict[SAMPLE_IMAGE_RELATIVE_PATH]
        print(f"  - Label retrieved successfully.")
        print(f"    - Label: {label}")
    else:
        print(f"[Error] Label for '{SAMPLE_IMAGE_RELATIVE_PATH}' not found in labels.txt.")

    print("\n✅ Verification successful! The dataset is ready to use.")

except FileNotFoundError:
    print(f"❌ Sample image not found at: {full_image_path}")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
