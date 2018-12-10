import pymongo

client = pymongo.MongoClient()
db = client.comic

def insert_comic(comic_dict):
    db.company.insert_one(comic_dict)