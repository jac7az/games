import json
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import zipfile
import os
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("game_processing.log"),
        logging.StreamHandler()                   
    ]
)
logging.info("Connecting to mongo.")

mongopw=os.environ.get("MONGOPW")
uri=f"mongodb+srv://jac7az_db_user:{mongopw}@cluster0.hevn98o.mongodb.net/"
client=pymongo.MongoClient(uri,server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    logging.error("Failed:",e)

logging.info("Uploading data")
db=client['game_database']
games=db['game_data']
folder='game_documents.zip'
batch_size=500
batch=[]
if not os.path.exists(folder):
    print(f"{folder} not found")
else:
    with zipfile.ZipFile(folder, 'r') as z:
        files=[f for f in z.namelist() if f.endswith('.json')]
        print(f"Uploading {len(files)} files")
        for i, filename in enumerate(files):
            try:
                with z.open(filename) as f:
                    game_record = json.load(f)
                    batch.append(game_record)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        if len(batch) >= batch_size:
            try:
                games.insert_many(batch)
                logging.info(f"Uploaded {i + 1} records...")
            except Exception as e:
                logging.error(f"Batch upload failed (likely a giant file): {e}\nTip: If this keeps failing, use insert_one instead of insert_many.")
            batch = []
        if batch:
            games.insert_many(batch)
            logging.info("insert complete")
print(games.find_one())
# games.delete_many({})
# print("Collection cleared")
