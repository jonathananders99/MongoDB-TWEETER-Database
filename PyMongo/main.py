from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Connects to online MongoDB cluster
client = MongoClient("mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority")


# Uses database TWEETER
db = client["TWEETER"]


# Get a list of the collections in the database
collections = db.list_collections()

# Iterate through the collections and print the name and validation rules
for collection in collections:
    name = collection["name"]
    options = collection["options"]
    if "validator" in options:
        print(f"Collection name: {name}")
        print(f"Validation rules: {options['validator']}")
    else:
        print(f"The '{name}' collection does not have any validation rules.")





# QUERIES

# All users with above 5000 followers, only return usernames, and follower count. 
# Sort by follower count
results = db["USER"].find(
    {
        "$and": [
            {"followers": {"$gt": 5000}},
        ]
    },
    {
        "_id": 0,
        "username": 1,
        "followers": 1
    }
).sort("followers", -1)
# Iterate through 5 of the results and print each document
for i in range(5):
    print(results[i])


# All replies from one user that were updated at least once, only return ids
results = db["REPLY"].find(
    {
        "$and": [
            {"user_id": ObjectId("60c714351b4f61adc8f6622f")},
            {"date_updated": {"$ne": None}}
        ]
    },
    {"_id": 1}
)
# Iterate through the results and print each document
for result in results:
    print(result)


# All of a user's followers, returns only followers ids
results = db["FOLLOWER"].find(
    {
        "$and": [
            {"user_id": ObjectId("d635031a11e52d3b81688e6e")}
        ]
    },
    {"follower_id": 1, "_id": 0}
)
# Iterate through the results and print each document
for result in results:
    print(result)
    

# All users with less than 7500 followers with more than 5000 favorites for users created from 
# current date to 2020-12-10, return usernames
results = db["USER"].find(
    {
        "$and": [
            {"followers": {"$lt": 7500}},
            {"favorites": {"$gt": 5000}},
            {"created": {
                "$gt": datetime.datetime(2020, 12, 10),
                "$lt": datetime.datetime.now()
            }
            }
        ]
    },
    {"_id": 0, "username": 1}
)
# Iterate through the results and print each document
for result in results:
    print(result)


# All tweets from last 5 years for one person
results = db["TWEET"].find(
    {
        "$and": [
            {
                "user_id": ObjectId("80629ffc3c0f4c28aa386662")
            },
            {
                "creation_date": {
                    "$gt": datetime.datetime(2017, 12, 10),
                    "$lt": datetime.datetime.now()
                }
            }
        ]
    }
)
# Iterate through the results and print each document
for result in results:
    print(result)


# Which user has the most amount of tweets
results = db["TWEET"].aggregate([
  {"$sortByCount": "$user_id"},
  {"$limit":1}
])
# Iterate through the results and print each document
for result in results:
    print(result)


# Top 10 tweets with the most replies
results = db["TWEET"].aggregate(
    [
        {
            "$project": {
                "replies_count": {
                    "$size": {
                        "$ifNull": ["$replies", []]
                    }
                }
            }
        },
        {
            "$sort": {"replies_count": -1}
        },
        {
            "$limit": 10
        }
    ]
)
# Iterate through the results and print each document
for result in results:
    print(result)


# All Tweets with 10 or more than favorites, return fav counts and ids, sort by fav count desc using $sort in pipeline
results = db["TWEET"].aggregate(
    [
        {
            "$project" : { "favorites_count": {"$size": {"$ifNull": ["$favorites", []]}}}
        }, 
        {
            "$match" : { "favorites_count" : { "$gte": 10 } }
        },
        {
            "$sort": {"favorites_count": -1}
        }
    ]
)
# Iterate through the results and print each document
for result in results:
    print(result)





# UPDATING DOCUMENTS and FUNCTIONS

# imitates a trigger for an on deletion of a document in TWEET collection
# move a tweet meant for deletion to the trashcan after necessary modification and delete it from tweet collection
def tweetTrash(tweetId):
    # Get the first document from the cursor
    tweet = db["TWEET"].aggregate([ 
        {
            "$match" : {
                "_id": tweetId
            }
        },
        {
            "$addFields": 
            { 
                "_id" : ObjectId(),
                "personnel": "admin1",  
                "deletion_date": datetime.datetime.now(),
                "old_id": tweetId
            }
        }
    ]).next()
    
    # Insert the modified document into the "TRASHCAN" collection
    db["TRASHCAN"].insert_one(tweet)
    
    # Delete the document from the "TWEET" collection
    db["TWEET"].delete_one({"_id": tweetId})
    print("Tweet has been moved to trashcan")

#test
tweetTrash(ObjectId("4aad42147a8f3e8ba32028fd"))


# given the id of a user increase the follower count by one
def incFollower(curId):
    db["USER"].update_one(
        {"_id": curId},
        {"$inc": {"followers": 1}}
    )
    print(f"Follower count incremented by 1 for document with id: {curId}")
# test
incFollower(ObjectId("d635031a11e52d3b81688e6e"))


# given the id of a user increase the following count by one
def incFollowing(curId):
    db["USER"].update_one(
        {"_id": curId},
        {"$inc": {"following": 1}}
    )
    print(f"Following count incremented by 1 for document with id: {curId}")
# test
incFollowing(ObjectId("d635031a11e52d3b81688e6e"))


# imitates a trigger for an insert into FOLLOWER
def insertIntoFollower(doc):
    # inserts document
    db["FOLLOWER"].insert_one(doc)
    print("Document with id: {} inserted into FOLLOWER collection".format(doc["_id"]))
    # increment follower count
    incFollower(doc["user_id"])
    # increment following count
    incFollowing(doc["follower_id"])
# test
insertIntoFollower(
    {
        "_id": ObjectId("ba9c74bcd388d8cc66d03904"),
        "user_id": ObjectId("018ea6a44222d47078ba8334"),
        "follower_id": ObjectId("c1511c0be859be2b841f9901"),
        "date_followed": datetime.datetime.strptime("2009-02-15", "%Y-%m-%d")
    }
)


# deletes any document in TRASHCAN with a deletion date of over 30 days ago or older.
def trashDelete30Days():
    delCount = db["TRASHCAN"].delete_many(
        { 
            "deletion_date": 
            { 
                "$lte": datetime.datetime.now() - datetime.timedelta(days=30) 
            } 
        }
    ).deleted_count
    print(f'{delCount} documents deleted from the trashcan')
# test
trashDelete30Days()