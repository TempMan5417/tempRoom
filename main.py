gifrom pymongo import MongoClient

url = "mongodb://jincheol:work930417@ds149593.mlab.com:49593/heroku_k0cr1wdd?retryWrites=false"
client = MongoClient(url)
db = client['heroku_k0cr1wdd']
collection = db['Test']

collection.insert_one( {'a':'b'} )
rows = collection.find({})
for row in rows:
  print (row)

