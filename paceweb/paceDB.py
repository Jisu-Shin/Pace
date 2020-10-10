from pymongo import MongoClient
import requests

#DB생성
client = MongoClient("mongodb://localhost:27017/")
projectdb = client['pace']
proCol = projectdb['customers']
firstcustomer = proCol.insert_one({"personalNum":0, "point": 0})
#print(client.list_database_names())
print(firstcustomer.inserted_id)
#number=0
#point = 0


#doc = {
  #  'PersonalNum' : number,
   # 'Point' : point
#}
#db.customer.insert_one(doc)
