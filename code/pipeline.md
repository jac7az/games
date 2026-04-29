```
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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
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

logging.info("Creating dataframe")
data = list(game.find({}))
df = pd.DataFrame(data)

logging.info("Editing dataframe to match platforms to each game, creating a row per different console for the same games")
df=df.explode('platforms')
row=pd.json_normalize(df['platforms'])
df=pd.concat([df.drop(columns=['platforms','_id']).reset_index(drop=True),row.reset_index(drop=True)],axis=1)

logging.info("Encoding nonnumeric data")
publisher_mean=df.groupby('publisher')['total_sales'].mean()
developer_mean=df.groupby('developer')['total_sales'].mean()
df['publisher_power']=df['publisher'].map(publisher_mean)
df['developer_power']=df['developer'].map(developer_mean)
le=LabelEncoder()
df['genre_encoded']=le.fit_transform(df['genre'])
df['console_encoded']=le.fit_transform(df['console'])
features=['critic_score', 'publisher_power', 'genre_encoded', 'console_encoded', 'release_year']
X=df[features]
y=df['total_sales']

logging.info("Training Random Forest Regressor Model without developer variable")
X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=756)
model=RandomForestRegressor(n_estimators=100,random_state=54)
model.fit(X_train,y_train)
importances=model.feature_importances_
features_df=pd.DataFrame({"Features": features, "Weights": importances}).sort_values(by="Weights")

logging.info("Creating feature importance barplot")
plt.figure(figsize=(10,10))
plt.barh(features_df['Features'],features_df['Weights'])
plt.title("Predictors of Video Game Sales (No Developer)")
plt.xlabel("Weight Influence")
plt.tight_layout()
plt.savefig("feature_importance_nodeveloper.png")
plt.show()

features2=['critic_score', 'publisher_power', 'developer_power','genre_encoded', 'console_encoded', 'release_year']
X=df[features2]
y=df['total_sales']

logging.info("Training Random Forest Regressor Model with developer variable")
X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=756)
model=RandomForestRegressor(n_estimators=100,random_state=54)
model.fit(X_train,y_train)
importances=model.feature_importances_
features_df=pd.DataFrame({"Features": features2, "Weights": importances}).sort_values(by="Weights")

logging.info("Creating feature importance barplot with developer")
plt.figure(figsize=(10,10))
plt.barh(features_df['Features'],features_df['Weights'])
plt.title("Predictors of Video Game Sales")
plt.xlabel("Weight Influence")
plt.tight_layout()
plt.savefig("feature_importance_developer.png")
plt.show()
```
## Analysis Rationale
Used a Random Forest Regressor to capture nonlinear relationships between the features, including interactions between developers, publisher, and critic scores. To avoid having high dimensionality and cardinality from encoding developers, publishers, consoles, and other qualitative variables, developers and publishers used their mean average sales as a proxy for their weight in the market. To find how influential each variable is, Feature Importance was used rather than a different metric because feature importance can directly identify how much each variable contributes to a model predicting sales price, which provides a more relevant answer to the specific problem.

An additional part of the analysis not mentioned in the Press Release is the difference between the developer and publisher. In the visualization without the developer variable, the publisher had the highest feature importance weight, but it was reduced to the lowest when the developer variable was added. This provides an insight into the high collinearity between publisher and developer, where it was actually the developer pushing the publisher's influence up.

## Visualization Rationale
A horizontal bar chart was chosen to display feature importance for easy comparison between weights of different variables, using the length of each bar to display how much weight each feature had in the overall prediction of total sales. The data was sorted from highest to lowest influence, matching the visual hierarchy of most to least important. The chart has a simplistic overall look to support easy reading for any end-user who discovers this research, including people with little data background.
