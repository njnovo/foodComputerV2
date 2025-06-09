from imageProcess import capture_images_and_compute_ndvi
from temp_hum import get_temp
from temp_hum import get_hum
from save_to_db import save_to_db
import os
import pandas as pd
import time
from datetime import datetime, timedelta

def collect_data():
    fc_num = input("which food computer is being measured")
    rgb_img, nir_img, ndvi_gray, ndvi_color, avg_ndvi, timestamp = capture_images_and_compute_ndvi()

    df_path = 'ndvi_data.csv'  # Define the path at the top

    new_entry = {
        'timestamp': timestamp,
        'rgb_image': rgb_img,
        'nir_image': nir_img,
        'ndvi_gray': ndvi_gray,
        'ndvi_color': ndvi_color,
        'average_ndvi': avg_ndvi,
        'temperature': get_temp(fc_num),
        'humidity': get_hum(fc_num),
        'food_computer': fc_num
    }

    # Load or create DataFrame
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
    else:
        df = pd.DataFrame(columns=list(new_entry.keys()))

    # Convert new_entry to DataFrame and append
    new_df = pd.DataFrame([new_entry])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(df_path, index=False)
    
    # Save to database
    save_to_db(new_entry)

def main():
    while True:
        print(f"Starting data collection at {datetime.now()}")
        collect_data()
        print(f"Data collection completed at {datetime.now()}")
        
        # Calculate next run time (2 days from now)
        next_run = datetime.now() + timedelta(days=2)
        print(f"Next data collection scheduled for {next_run}")
        
        # Sleep until next run time
        time.sleep(2 * 24 * 60 * 60)  # Sleep for 2 days in seconds

if __name__ == "__main__":
    main() 