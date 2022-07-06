from pymongo import MongoClient
client=MongoClient('mongodb://localhost',27017)

my_database=client['myDatabase']
#or 
#my_database=client.myDatabase

my_collection=my_database['student']
#or 
#my_collection=my_database.student

print(client.list_database_names())
print(my_database.list_collection_names())


# #insert one record
# record_id=my_collection.insert_one({"name":"Kitan","age":28})    
# print(record_id.inserted_id) 

# #insert multiple records
# mylist = [
#   { "name": "Amy", "age": 25},
#   { "name": "Hannah", "age": 45},
#   { "name": "Michael", "age": 23},
#   { "name": "Sandy", "age": 33},
#   { "name": "Betty", "age": 21},
#   { "name": "Richard", "age": 28},
#   { "name": "Susan", "age": 55},
#   { "name": "Vicky", "age": 45},
#   { "name": "Ben", "age": 33},
#   { "name": "William", "age": 24},
#   { "name": "Chuck", "age": 55},
#   { "name": "Viola", "age": 45}
# ]

# rec_id=my_collection.insert_many(mylist)
# print(rec_id.inserted_ids)

# my_list = [
#   { "_id":1,"name": "Amy", "age": 25},
#   { "_id":2,"name": "Hannah", "age": 45},
#   { "_id":3,"name": "Michael", "age": 23},
#   { "_id":4,"name": "Sandy", "age": 33},
#   { "_id":5,"name": "Betty", "age": 21},
#   { "_id":6,"name": "Richard", "age": 28},
#   { "_id":7,"name": "Susan", "age": 55},
#   { "_id":8,"name": "Vicky", "age": 45},
#   { "_id":9,"name": "Ben", "age": 33},
#   { "_id":10,"name": "William", "age": 24},
#   { "_id":11,"name": "Chuck", "age": 55},
#   { "_id":12,"name": "Viola", "age": 45}
# ]

# ids=my_collection.insert_many(my_list)
# print(ids.inserted_ids)


# #print all fields
# for x in my_collection.find():
#     print(x)

# #2nd parameter is used to include the fields to print
# for x in my_collection.find({},{"_id":0,"name":1}):
#     print(x)

#print only one document
print(my_collection.find_one())

#Query the database / Filter
values=my_collection.find({"age":23})     #prints all records with age 23
for x in values:
    print(x)

#Advanced filters & queries using regex & matching

filter1={"name":{"$gt":"S"}}
filter2={"name":{"$regex":"^R"}}

values1=my_collection.find(filter1)
values2=my_collection.find(filter2)

for x in values1:
    print(x)

for i in values2:
    print(i)


#sort the data default is ascending:sort(filed_name,1) descending:sort(field_name,-1)
sorted1=my_collection.find().sort("name")
for i in sorted1:
    print(i)


#Delete 

delete_query1={"name":"Ravi"}
delete_query2={"name":{"$regex":"^S"}}
delete_all={}

d1=my_collection.delete_one(delete_query1)
d2=my_collection.delete_many(delete_query2)
print(d1.deleted_count)
print(d2.deleted_count)

#update query

update_one_query={"age":"23"}
new_age={"$set":{"age":33}}

update_many_query={"name":{"$regex":"^D"}}
new_name={"$set":{"name":"Kiran"}}

u1=my_collection.update_one(update_one_query,new_age)
u2=my_collection.update_many(update_many_query,new_name)

print(u1.modified_count)
print(u2.modified_count)

#limit a query result
res=my_collection.find({"name":{"$regex":"^A"}}).limit(3)
for i in res:
    print(i)


#drop a collection
my_collection.drop()


