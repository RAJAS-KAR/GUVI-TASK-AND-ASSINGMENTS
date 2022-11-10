!pip install pymongo
import pymongo
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = client["Employee"]
information = mydb.employeeinformation
record = {
    "firstname" : 'eneeyan',
        "city" : 'chennai'
}
information.insert_one(record)
