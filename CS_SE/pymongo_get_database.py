from pymongo import MongoClient
from pandas import DataFrame
CONNECTION_STRING = "mongodb://azure-web-project:M73MVy790iHsITudPP4Q1xOeGjKLLeDueOKDM3h9hzZm0zmU8t1Ffc0uhTBFGQ74wz43RE8Shc6oACDbPizDQw==@azure-web-project.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azure-web-project@"
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://azure-web-project:M73MVy790iHsITudPP4Q1xOeGjKLLeDueOKDM3h9hzZm0zmU8t1Ffc0uhTBFGQ74wz43RE8Shc6oACDbPizDQw==@azure-web-project.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azure-web-project@"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)

   return client['CS_SE']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
