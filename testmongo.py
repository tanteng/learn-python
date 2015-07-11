
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://tanteng:123456@localhost:27017/')
db = client.js_send_excel

post = {"author": "Xiaofeng", "text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"],}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)