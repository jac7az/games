import pandas as pd
import json
import os
import shutil
from google.colab import files
df = pd.read_csv('Video_Games_Sales_Cleaned.csv')
df=df[df['release_year']>2009]
output_dir = 'game_documents'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for index, row in df.iterrows():
    clean_title = "".join([c for c in str(row['title']) if c.isalnum() or c in (' ', '_')]).strip()
    filename = f"{index}_{clean_title}.json"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        json.dump(row.to_dict(), f, indent=4)

print(f"Created {len(df)} JSON documents in the '{output_dir}' folder.")
folder_to_zip = 'game_documents'
output_filename = 'game_documents_archive'
shutil.make_archive(output_filename, 'zip', folder_to_zip)

files.download(f'{output_filename}.zip')
