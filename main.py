from pymongo import MongoClient

url = "mongodb://jincheol:work930417@ds149593.mlab.com:49593/heroku_k0cr1wdd?retryWrites=false"
client = MongoClient(url)
db = client['heroku_k0cr1wdd']
collection = db['Test']

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# collection.insert_one({'name':'bobby','age':21})
# collection.insert_one({'name':'kay','age':27})
# collection.insert_one({'name':'john','age':30})
# db.Test.insert_one({'name':'test','age':30})

# # ttt
# collection.insert_one( {'a':'b'} )

rows = collection.find({})

# for row in rows:
#   print (row)



# 문제1 : 바디라는 이름을 가진 애 출력.
# for row in rows:
#   # 필터
#   if 'name' not in row : continue

#   # 실행 
#   curName = row['name']
#   if curName == 'bobby' :
#     print (row)


# # 문제2 : 21살보다 많으면.
# for row in rows:
#   # 필터
#   if 'age' not in row : continue

#   # 실행 
#   curAge = row['age']
#   if curAge > 21 :
#     print (row)

# # 문제3 : 21살보다 많고 가장 나이가 많은 사람.


# hasAgeDataList = [ row for row in rows if 'age' in row ]
# hasAgeDataList_over21 = [ row for row in hasAgeDataList if row['age'] > 21 ] 

# ageDataList = [ row['age'] for row in hasAgeDataList_over21 ]
# maxAge = max(ageDataList)

# # print
# for row in hasAgeDataList_over21:
#   if row['age'] == maxAge :
#     print (row)

# 문제4 : 21살보다 많고 가장 나이가 많은 사람의 갯수를 찾기

# filtering
hasAgeDataList = [ row for row in rows if 'age' in row ]
hasAgeDataList_over21 = [ row for row in hasAgeDataList if row['age'] > 21 ] 

ageDataList = [ row['age'] for row in hasAgeDataList_over21 ]
maxAge = max(ageDataList)
resultList = []

num = 0
# get info
for row in hasAgeDataList_over21:
  if row['age'] == maxAge :
    num += 1
    
print (num)

# output  
