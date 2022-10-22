import pymongo
from django.views.generic import View


client = pymongo.MongoClient('mongodb+srv://staybility:staybility21db@secoundhouse.wwk6htb.mongodb.net/test')
#Define DB Name
dbname = client['test_db']

#Define Collection
collection = dbname['mascot']

class Mongo(View):
	def get(self, request):
		mascot_1={
			"name": "Sammy",
			"type" : "Shark",
			"test":["aa","bb"],
			"address":{
				"aaa":"bbb",
				"ccc":"ddd"
			}
		}

		collection.insert_one(mascot_1)

		mascot_details = collection.find({})
		print(mascot_details)