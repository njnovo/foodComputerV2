import cv2
import numpy as np

def get_ndvi(image1, image2, out_file_gray, out_file_color, threshold=0.3):
    """
    Calculate NDVI from RGB and NIR images using OpenCV, apply threshold to isolate plants,
    and compute average NDVI for those pixels. Saves both grayscale and color NDVI images.
    
    Parameters:
    - image1: Path to RGB image
    - image2: Path to NIR image
    - out_file_gray: Path to save grayscale NDVI image
    - out_file_color: Path to save color NDVI image
    - threshold: NDVI threshold to identify plants (default = 0.3)
    """

    # Read images as float32 for NDVI calculations
    rgb = cv2.imread(image1).astype(np.float32)
    nir = cv2.imread(image2).astype(np.float32)

    # Calculate average of NIR image across channels
    nir_avg = np.mean(nir, axis=2)

    # Extract red channel from RGB image (OpenCV loads in BGR order)
    red = rgb[:, :, 2]

    # Avoid divide-by-zero
    bottom = nir_avg + red
    bottom[bottom == 0] = 0.01 # small epsilon

    # NDVI calculation
    ndvi = (nir_avg - red) / bottom
    ndvi = np.clip(ndvi, -1.0, 1.0)

    # Thresholding to identify plants
    plant_mask = ndvi >= threshold
    plant_ndvi_values = ndvi[plant_mask]

    # Average NDVI of detected plants
    average_ndvi = np.mean(plant_ndvi_values) if plant_ndvi_values.size > 0 else 0

    # Scale NDVI to 0–255 for visualization
    ndvi_vis = ((ndvi + 1) / 2 * 255).astype(np.uint8)

    # Save grayscale NDVI image
    cv2.imwrite(out_file_gray, ndvi_vis)

    # Apply colormap (e.g., JET) for better visualization
    ndvi_color = cv2.applyColorMap(ndvi_vis, cv2.COLORMAP_JET)
    cv2.imwrite(out_file_color, ndvi_color)

    print(f"Average NDVI of detected plants (NDVI > {threshold}): {average_ndvi:.3f}")
    return average_ndvi

