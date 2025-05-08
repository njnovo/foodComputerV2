import os
from datetime import datetime
import subprocess

def capture_images_and_compute_ndvi(ndvi_fn, df_path='ndvi_data.csv', threshold=0.3):
    """
    Captures images from Pi Camera ports, computes NDVI, and logs results to a DataFrame.

    Parameters:
    - ndvi_fn: NDVI function reference (like get_ndvi)
    - df_path: Path to save the CSV file of NDVI results
    - threshold: NDVI threshold for plant detection
    """

    # Set filenames
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    rgb_img = f'rgb_{timestamp}.jpg'
    nir_img = f'nir_{timestamp}.jpg'
    ndvi_gray = f'ndvi_gray_{timestamp}.png'
    ndvi_color = f'ndvi_color_{timestamp}.png'

    # Capture RGB image from Pi camera port 2
    subprocess.run([
        'libcamera-still',
        '--camera', '1', # port 2 = index 1
        '-o', rgb_img,
        '--width', '640',
        '--height', '480',
        '--nopreview',
        '--timeout', '1000'
    ], check=True)

    # Capture NIR image from Pi camera port 1
    subprocess.run([
        'libcamera-still',
        '--camera', '0', # port 1 = index 0
        '-o', nir_img,
        '--width', '640',
        '--height', '480',
        '--nopreview',
        '--timeout', '1000'
    ], check=True)

    # Compute NDVI and get average
    avg_ndvi = ndvi_fn(rgb_img, nir_img, ndvi_gray, ndvi_color, threshold=threshold)

    return rgb_img, nir_img, ndvi_gray, ndvi_color, avg_ndvi, timestamp
