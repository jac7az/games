import pandas as pd
import numpy as np
import os
import logging
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

#Creating log file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()                   
    ]
)

#Connecting to mongo server database
try:
    mongopw = os.environ.get("MONGOPW")
    uri = f"mongodb+srv://jac7az_db_user:{mongopw}@cluster0.hevn98o.mongodb.net/"
    client = MongoClient(uri)
    db = client['game_database']
    game = db['game_data']
    logging.info("Connection established")
except Exception as e:
    logging.error("Couldn't connect to mongo")

#Create dataframe from the JSON docs
logging.info("Creating dataframe")
data = list(game.find({}))
df = pd.DataFrame(data)

#Flattening and resplitting so that each console per game will become its own row
logging.info("Editing dataframe to match platforms to each game, creating a row per different console for the same games")
df=df.explode('platforms')
row=pd.json_normalize(df['platforms'])
df=pd.concat([df.drop(columns=['platforms','_id']).reset_index(drop=True),row.reset_index(drop=True)],axis=1)

#Mapping mean sales for publisher and developer to its company as the proxy for market influence
logging.info("Encoding nonnumeric data")
publisher_mean=df.groupby('publisher')['total_sales'].mean()
developer_mean=df.groupby('developer')['total_sales'].mean()
df['publisher_power']=df['publisher'].map(publisher_mean)
df['developer_power']=df['developer'].map(developer_mean)

#Encoding rest of the categorical features
le=LabelEncoder()
df['genre_encoded']=le.fit_transform(df['genre'])
df['console_encoded']=le.fit_transform(df['console'])

#Establishing x and y, no developer version
features=['critic_score', 'publisher_power', 'genre_encoded', 'console_encoded', 'release_year']
X=df[features]
y=df['total_sales']

#Model train test split for analysis and fitting random forest regressor
logging.info("Training Random Forest Regressor Model without developer variable")
X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=756)
model=RandomForestRegressor(n_estimators=100,random_state=54)
model.fit(X_train,y_train)

#Capturing feature importance 
importances=model.feature_importances_
features_df=pd.DataFrame({"Features": features, "Weights": importances}).sort_values(by="Weights")

#plotting feature importance bar graph
logging.info("Creating feature importance barplot")
plt.figure(figsize=(10,10))
plt.barh(features_df['Features'],features_df['Weights'])
plt.title("Predictors of Video Game Sales (No Developer)")
plt.xlabel("Weight Influence")
plt.tight_layout()
plt.savefig("feature_importance_nodeveloper.png")
plt.show()

#analysis version 2: random forest regressor with developer
features2=['critic_score', 'publisher_power', 'developer_power','genre_encoded', 'console_encoded', 'release_year']
X=df[features2]
y=df['total_sales']

#Model train test split for analysis and fitting random forest regressor
logging.info("Training Random Forest Regressor Model with developer variable")
X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=756)
model=RandomForestRegressor(n_estimators=100,random_state=54)
model.fit(X_train,y_train)

#Capturing feature importance 
importances=model.feature_importances_
features_df=pd.DataFrame({"Features": features2, "Weights": importances}).sort_values(by="Weights")

#Plotting feature importance
logging.info("Creating feature importance barplot with developer")
plt.figure(figsize=(10,10))
plt.barh(features_df['Features'],features_df['Weights'])
plt.title("Predictors of Video Game Sales")
plt.xlabel("Weight Influence")
plt.tight_layout()
plt.savefig("feature_importance_developer.png")
plt.show()
