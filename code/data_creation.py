import pandas as pd
import json
import os
import shutil
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("game_processing.log"),
        logging.StreamHandler()                   
    ]
)
logging.info("Converting to JSON.")

try:
    df = pd.read_csv('Video_Games_Sales_Cleaned.csv')
    df = df[df['release_year'] > 2009]
    logging.info(f"Data loaded and filtered successfully")
except Exception as e:
    logging.error("Failed to load CSV")

output_dir = 'game_documents'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for title, group in df.groupby('title'):
    clean_title = "".join([c for c in str(title) if c.isalnum() or c in (' ', '_')]).strip()
    filename = f"{clean_title}.json"
    filepath = os.path.join(output_dir, filename)
    
    document = {
        "title": title,
        "genre": group['genre'].iloc[0],
        "publisher": group['publisher'].iloc[0],
        "developer": group['developer'].iloc[0],
        "platforms": []
    }
    
    for _, row in group.iterrows():
        platform_info = {
            "console": row['console'],
            "total_sales": row['total_sales'],
            "critic_score": float(row['critic_score']), 
            "release_year": int(row['release_year'])
        }
        document["platforms"].append(platform_info)
    
    with open(filepath, 'w') as f:
        json.dump(document, f, indent=4)

logging.info(f"Created {len(df.groupby('title'))} platform-accurate JSON documents.")

try:
    output_filename = 'game_documents_combined_archive'
    shutil.make_archive(output_filename, 'zip', output_dir)
    #files.download(f'{output_filename}.zip')
    logging.info("Successfully created zip folder")
    shutil.rmtree(output_dir)
    logging.info(f"Temporary directory {output_dir} removed.")
except Exception as e:
    logging.error("Failed to create zip folder")
