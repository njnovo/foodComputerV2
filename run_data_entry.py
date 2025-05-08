from imageProcess import capture_images_and_compute_ndvi
from temp_hum import get_temp
from temp_hum import get_hum
from save_to_db import save_to_db

fc_num = input("which food computer is being measured")
rgb_img, nir_img, ndvi_gray, ndvi_color, avg_ndvi, timestamp = capture_images_and_compute_ndvi()

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
if(os.path.exists(df_path):
    df = pd.read_csv(df_path)
else:
    df = pd.DataFrame(columns=new_entry.keys())

# Append new data
df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
df.to_csv(df_path, index=False)

print(f"Logged NDVI data at {timestamp} with average NDVI: {avg_ndvi:.3f}")

save_to_db()