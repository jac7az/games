import pandas as pd
import numpy as np
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
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

try:
    mongopw = os.environ.get("MONGOPW")
    uri = f"mongodb+srv://jac7az_db_user:{mongopw}@cluster0.hevn98o.mongodb.net/"
    client = MongoClient(uri)
    db = client['game_database']
    game = db['game_data']
    logging.info("Connection established")
except Exception as e:
    logging.error("Couldn't connect to mongo")

data = list(game.find())
df = pd.DataFrame(data)

df=df.explode('platforms')
row=pd.json_normalize(df['platforms'])
df=pd.concat([df.drop(columns=['platforms','_id']).reset_index(drop=True),row.reset_index(drop=True)],axis=1)
df=df[df['total_sales']>0]

top_publishers=df['publisher'].value_counts().nlargest(15).index
df['brands']=df['publisher'].apply(lambda x: x if x in top_publishers else 'Other')
X=pd.get_dummies(df[['brands']],drop_first=True)
y=df['total_sales']
scaler=StandardScaler()
X_scale=scaler.fit_transform(X)
model=LinearRegression()
model.fit(X_scale,y)
weights=pd.DataFrame({"Feature":X.columns,"Weight":model.coef_}).sort_values(by='Weight')

counts = df['brands'].value_counts().reset_index()
counts.columns = ['Publisher', 'Count']
brand_results = weights[weights['Feature'].str.contains('brands')]
brand_results['Publisher'] = brand_results['Feature'].str.replace('brands', '')
comparison_df=pd.merge(brand_results,counts,on='Publisher')
print(comparison_df)