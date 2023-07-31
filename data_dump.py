import pymongo
import pandas as pd
import json
from insurance.config import mongo_client

# Provide the mongodb localhost url to connect python to mongodb.
client = ("mongodb+srv://himanshu:himanshu12345@ineuron.fpig7r5.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME = "insurance"
COLLECTION_NAME = "premium"
DATA_FILE_PATH = "/config/workspace/insurance_main_dataset.csv"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}" )

    #Convert dataframe into JSON so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values()) 
    print(json_record[0])

    #insert converted json to mongo db  
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

