import os
import pandas as pd
from datetime import datetime
import subprocess
from get_ndvi import get_ndvi

def capture_images_and_compute_ndvi(ndvi_fn, fc, df_path='ndvi_data.csv', threshold=0.3):
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

    # Prepare data entry
    # FC1 is low FC2 is high FC3 is control
    new_entry = {
        'timestamp': timestamp,
        'rgb_image': rgb_img,
        'nir_image': nir_img,
        'ndvi_gray': ndvi_gray,
        'ndvi_color': ndvi_color,
        'average_ndvi': avg_ndvi,
        'food_computer': fc
    }

    # Load or create DataFrame
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
    else:
        df = pd.DataFrame(columns=new_entry.keys())

    # Append new data
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(df_path, index=False)

    print(f"Logged NDVI data at {timestamp} with average NDVI: {avg_ndvi:.3f}")
    return df

#only manual input for now
fc_num = input("which food computer is being measured")
capture_images_and_compute_ndvi(get_ndvi(), fc_num)