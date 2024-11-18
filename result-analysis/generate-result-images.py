import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pydicom
import sys

# Compressed directories and extensions
compressed_directories_base = {
    "png": "-png-compressed",
    "jpeg": "-jpeg-compressed",
    "pca95": "-pca-compressed-950",
    "pca975": "-pca-compressed-975",
    "pca99": "-pca-compressed-990",
}

compressed_extensions = {
    "png": ".png",
    "jpeg": ".jpeg",
    "pca95": ".npz",
    "pca975": ".npz",
    "pca99": ".npz",
}


# Function to read DICOM images
def read_dicom_image(path):
    ds = pydicom.dcmread(path)
    image = ds.pixel_array
    return (image - np.min(image)) / (np.max(image) - np.min(image)) * 255


# Function to read PNG and JPEG images
def read_image(path):
    return np.array(Image.open(path).convert("L"))


# Function to reconstruct PCA images
def read_pca_image(path):
    data = np.load(path)
    compressed_image = data["compressed_image"]
    principal_components = data["principal_components"]
    mean = data["mean"]
    reconstructed_image = np.dot(compressed_image, principal_components) + mean
    return np.clip(reconstructed_image, 0, 255)


# Function to get the file size in KB and compression ratio
def get_file_details(original_path, compressed_path):
    if os.path.exists(original_path) and os.path.exists(compressed_path):
        original_size = os.path.getsize(original_path)
        compressed_size = os.path.getsize(compressed_path)
        compression_ratio = 100 * (1 - compressed_size / original_size)
        return f"({compressed_size / 1024:.1f} KB, {compression_ratio:.1f}%)"
    elif os.path.exists(compressed_path):
        return f"({os.path.getsize(compressed_path) / 1024:.1f} KB)"
    return "(Not Found)"


# Function to find and display images
def find_and_save_images(dicom_path, output_path):
    if not os.path.exists(dicom_path):
        print(f"DICOM file not found: {dicom_path}")
        return

    # Extract directory and filename
    base_dir = os.path.dirname(dicom_path)
    file_name = os.path.basename(dicom_path)
    file_basename = os.path.splitext(file_name)[0]

    # Load the DICOM image
    images = []
    labels = []

    # Add DICOM image
    dicom_size = f"({os.path.getsize(dicom_path) / 1024:.1f} KB)"
    images.append(read_dicom_image(dicom_path))
    labels.append(f"DICOM - ORIGINAL {dicom_size}")

    # Search for compressed images
    for method, extension in compressed_extensions.items():
        compressed_directory = base_dir + compressed_directories_base[method]
        compressed_path = os.path.join(compressed_directory, file_basename + extension)

        if os.path.exists(compressed_path):
            if method.startswith("pca"):
                images.append(read_pca_image(compressed_path))
                labels.append(
                    f"PCA {method[-2:].replace('95', '95%').replace('99', '99%').replace('75', '97.5%')} "
                    f"{get_file_details(dicom_path, compressed_path)}"
                )
            else:
                images.append(read_image(compressed_path))
                labels.append(
                    f"{method.upper()} {get_file_details(dicom_path, compressed_path)}"
                )
        else:
            images.append(None)  # Mark as not found
            labels.append(f"{method.upper()} (Not Found)")

    # Create the figure in 2x3 layout with reduced gaps
    fig, axes = plt.subplots(
        2, 3, figsize=(15, 10), gridspec_kw={"hspace": 0.1, "wspace": 0.05}
    )
    axes = axes.flatten()
    for ax, image, label in zip(axes, images, labels):
        if image is not None:
            ax.imshow(image, cmap="gray")
        ax.set_title(label, fontsize=10)
        ax.axis("off")

    # Save the figure as an image file
    print(base_dir)
    plt.tight_layout()
    plt.savefig(
        f"./results/result-{base_dir.split('/').pop().split('-')[0]}",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()
    print(f"Image saved to {output_path}")


# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python display_images.py <path_to_dicom_file>")
        sys.exit(1)

    dicom_path = sys.argv[1]
    output_path = "./results/result.png"
    find_and_save_images(dicom_path, output_path)
