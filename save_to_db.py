import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def save_to_db(entry="ndvi_data.csv"):
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ndvi_data (timestamp, rgb_image, nir_image, ndvi_gray, ndvi_color, average_ndvi)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        (
            entry['timestamp'],
            entry['rgb_image'],
            entry['nir_image'],
            entry['ndvi_gray'],
            entry['ndvi_color'],
            entry['average_ndvi'],
            entry['food_computer']
        )
    )
    conn.commit()
    cur.close()
    conn.close()
