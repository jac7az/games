import json
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import zipfile
import os
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
logging.info("Connecting to mongo.")

#Retrieve password from environment then connect to database
mongopw=os.environ.get("MONGOPW")
uri=f"mongodb+srv://jac7az_db_user:{mongopw}@cluster0.hevn98o.mongodb.net/"
client=pymongo.MongoClient(uri,server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    logging.error("Failed:",e)

#Uploading data to a mongoDB database
logging.info("Uploading data")
db=client['game_database']
games=db['game_data']

#Naming the zip file to open and collect documents from 
folder='game_documents_combined_archive.zip'

#Maximum batch size to upload into mongodb in 1 round
batch_size=500
batch=[]
if not os.path.exists(folder):
    logging.error(f"{folder} not found")
else:
    #Process zip folder, opening each JSON file 
    with zipfile.ZipFile(folder, 'r') as z:
        files=[f for f in z.namelist() if f.endswith('.json')]
        logging.info(f"Uploading {len(files)} files")
        for i, filename in enumerate(files):
            try:
                with z.open(filename) as f:
                    game_record = json.load(f)
                    batch.append(game_record)
                
                #Bulk insertion for efficiency when batch size is met
                if len(batch) >= batch_size:
                    games.insert_many(batch)
                    logging.info(f"Uploaded {i + 1} records...")
                    batch = []
            except Exception as e:
                logging.error(f"Batch upload failed (likely a giant file): {e}\nTip: If this keeps failing, use insert_one instead of insert_many.")
        #Upload the remaining documents as part of the last batch
        if batch:
            games.insert_many(batch)
            logging.info("insert complete")
print(games.find_one())

##Optional data deletion if data needs to be purged for changes
# games.delete_many({})
# print("Collection cleared")
