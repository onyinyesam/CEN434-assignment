import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['friends']

collection = db['users']

user_data = [
    {"name": "nini", "age": 19},
    {"name": "chioma", "age": 21}
]
result = collection.insert_many(user_data)
print("Inserted IDs:", result.inserted_ids)

all_users = collection.find()
print("\nAll Users:")
for user in all_users:
    print(user)

query = {"name": "chioma"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)

query = {"name": "nini"}
new_values = {"$set": {"name": "NINI"}}
collection.update_one(query, new_values)

all_users_after_update = collection.find()
print("\nAll Users After Update:")
for user in all_users_after_update:
    print(user)


query = {"name": "chioma"}
collection.delete_one(query)
print("\nUser 'chioma' deleted.")
all_users_after_deletion = collection.find()
print("\nAll Users After Deletion:")
for user in all_users_after_deletion:
    print(user)