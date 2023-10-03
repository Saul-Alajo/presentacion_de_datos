

from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import certifi
load_dotenv()


user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASS')
db_hostname = os.getenv('MONGO_HOST')
ca=certifi.where()
uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"

# Send a ping to confirm a successful connection
def dbconnection():
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri, tlsCAFile=ca)
        db= client["PRODUCTOS"]
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return db

#if __name__ == "__main__":
#    MongoConnect().test_connection()
