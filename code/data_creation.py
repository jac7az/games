import pandas as pd
import json
import os
import shutil
import logging

#Creating log file
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
    #Load and filter dataset for only 2010-2020 data
    df = pd.read_csv('Video_Games_Sales_Cleaned.csv')
    df = df[df['release_year'] > 2009]
    logging.info(f"Data loaded and filtered successfully")
except Exception as e:
    logging.error("Failed to load CSV")

#Establish temporary directory for converting individual JSON documents
output_dir = 'game_documents'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#Grouping by title so one document will contain information for 1 game on all its consoles
for title, group in df.groupby('title'):
    clean_title = "".join([c for c in str(title) if c.isalnum() or c in (' ', '_')]).strip()
    filename = f"{clean_title}.json"
    filepath = os.path.join(output_dir, filename)
    
    #Establishing document structure
    document = {
        "title": title,
        "genre": group['genre'].iloc[0],
        "publisher": group['publisher'].iloc[0],
        "developer": group['developer'].iloc[0],
        "platforms": []
    }
    
    #Add specific sales and score data per console
    for _, row in group.iterrows():
        platform_info = {
            "console": row['console'],
            "total_sales": row['total_sales'],
            "critic_score": float(row['critic_score']), 
            "release_year": int(row['release_year'])
        }
        document["platforms"].append(platform_info)
    
    #Complete the JSON file
    with open(filepath, 'w') as f:
        json.dump(document, f, indent=4)

logging.info(f"Created {len(df.groupby('title'))} platform-accurate JSON documents.")

#Create output file into a single zip file with the option to autodownload it.
try:
    output_filename = 'game_documents_combined_archive'
    shutil.make_archive(output_filename, 'zip', output_dir)
    #files.download(f'{output_filename}.zip')
    logging.info("Successfully created zip folder")
    shutil.rmtree(output_dir)
    logging.info(f"Temporary directory {output_dir} removed.")
except Exception as e:
    logging.error("Failed to create zip folder")
