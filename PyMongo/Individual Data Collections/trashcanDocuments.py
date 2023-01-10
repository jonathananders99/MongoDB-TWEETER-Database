from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Connects to online MongoDB cluster
client = MongoClient("mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority")

# Uses database TWEETER
db = client["TWEETER"]

# Uses TRASHCAN collection
collection = db["TRASHCAN"]

# Insert the documents into the "TRASHCAN" collection
result = collection.insert_many(
    [
        {
            "_id": ObjectId("9a9de476c47d452703a45aa5"),
            "user_id": ObjectId("d3a9c688fcafbd306b7fece4"),
            "tweet": "Labore occaecat in aute duis id in",
            "favorites": [],
            "replies": [],
            "retweets": [],
            "mentions": [],
            "tags": [],
            "creation_date": datetime.datetime.strptime("2011-05-19", "%Y-%m-%d"),
            "edit_date": None,
            "personnel": 'admin1',
            "deletion_date": datetime.datetime.now(),
            "old_id": ObjectId("d23340a1580aa3de6ff9c7aa")
        },
        {
            "_id": ObjectId("f00b3eb2c8b7b3ead696ac98"),
            "user_id": ObjectId("18b0050cdf58331e1f37cb54"),
            "tweet": "Cupidatat duis veniam consectetur incididunt laboris",
            "favorites": [],
            "replies": [],
            "retweets": [],
            "mentions": [],
            "tags": [],
            "creation_date": datetime.datetime.strptime("2010-09-14", "%Y-%m-%d"),
            "edit_date": None,
            "personnel": 'admin1',
            "deletion_date": datetime.datetime.now(),
            "old_id": ObjectId("6974eabfe55bc355a2f0452f")
        },
        {
            "_id": ObjectId("7647e007fff292057914dfc3"),
            "user_id": ObjectId("b9ca703ab078531e67590ad3"),
            "tweet": "Est reprehenderit sit cupidatat et amet et, esse anim estdolore in eu laboris esse occaecat, ipsum qui non dolor eiusmod officia ipsum",
            "favorites": [],
            "replies": [],
            "retweets": [],
            "mentions": [],
            "tags": [],
            "creation_date": datetime.datetime.strptime("2015-10-07", "%Y-%m-%d"),
            "edit_date": None,
            "personnel": 'admin2',
            "deletion_date": datetime.datetime.now(),
            "old_id": ObjectId("e909e2b8427be87af3e1f5c4")
        },
        {
            "_id": ObjectId("f653e4c466c4e2207c4eef8e"),
            "user_id": ObjectId("80f6af96c4be88597823cb90"),
            "tweet": "Sunt voluptate aliqua pariatur",
            "favorites": [],
            "replies": [],
            "retweets": [],
            "mentions": [],
            "tags": [],
            "creation_date": datetime.datetime.strptime("2016-12-17", "%Y-%m-%d"),
            "edit_date": None,
            "personnel": 'admin1',
            "deletion_date": datetime.datetime.now(),
            "old_id": ObjectId("b36d62961783f4e42ab842c3")
        },
        {
            "_id": ObjectId("3f67d0110873d1069bf7acc3"),
            "user_id": ObjectId("4a58a74b41461ec37e60736e"),
            "tweet": "Laboris ea proident adipiscing fugiat incididunt Nonea sunt cupidatat, id anim est ipsum culpa velit nostrud in veniam consequat in Nonea esse",
            "favorites": [],
            "replies": [],
            "retweets": [],
            "mentions": [],
            "tags": [],
            "creation_date": datetime.datetime.strptime("2022-03-05", "%Y-%m-%d"),
            "edit_date": None,
            "personnel": 'admin2',
            "deletion_date": datetime.datetime.strptime("2022-10-15", "%Y-%m-%d"),
            "old_id": ObjectId("a6fd41b805c90f0dc37b3451")
        },
        {
            "_id": ObjectId("15bdf1c1369c487313f984fc"),
            "username": "Terry.Blankenship231",
            "first_name": "Terry",
            "last_name": "Blankenship",
            "email": "Terry.Blankenship231@company.com",
            "password": "AKT7G5U5BWMYDYU",
            "favorites": 4764,
            "followers": 1176,
            "following": 9576,
            "created": datetime.datetime.strptime("2015-07-03", "%Y-%m-%d"),
            "personnel": 'admin1',
            "deletion_date": datetime.datetime.now(),
            "old_id": ObjectId("c79a0457446fd4e0c5ad1fd8")
        },
        {
            "_id": ObjectId("e6828cab2748d59a9ee9c1ee"),
            "username": "Patrick.Austin92",
            "first_name": "Patrick",
            "last_name": "Austin",
            "email": "Patrick.Austin92@company.com",
            "password": "KSNABKQWQSEQAF8",
            "favorites": 6939,
            "followers": 98922,
            "following": 4738,
            "created": datetime.datetime.strptime("2016-11-29", "%Y-%m-%d"),
            "personnel": 'admin1',
            "deletion_date": datetime.datetime.now(),
            "old_id": ObjectId("88e3bf8612bf0a1098a910c4")
        },
        {
            "_id": ObjectId("c607650e76b0109c6e628873"),
            "username": "Beth.Moreno401",
            "first_name": "Beth",
            "last_name": "Moreno",
            "email": "Beth.Moreno401@company.com",
            "password": "35IRXDQYYWC45U2",
            "favorites": 1724,
            "followers": 2505,
            "following": 4173,
            "created": datetime.datetime.strptime("2014-12-20", "%Y-%m-%d"),
            "personnel": 'admin2',
            "deletion_date": datetime.datetime.strptime("2022-11-23", "%Y-%m-%d"),
            "old_id": ObjectId("3ae74c95ac964bd68fc8a3c6")
        },
        {
            "_id": ObjectId("5af98ad14811d28b0cccd6cc"),
            "username": "Stephen.Clark54",
            "first_name": "Stephen",
            "last_name": "Clark",
            "email": "Stephen.Clark54@company.com",
            "password": "14HTD8C5E4GYAXQ",
            "favorites": 1121,
            "followers": 52924,
            "following": 9458,
            "created": datetime.datetime.strptime("2017-07-22", "%Y-%m-%d"),
            "personnel": 'admin1',
            "deletion_date": datetime.datetime.strptime("2022-11-23", "%Y-%m-%d"),
            "old_id": ObjectId("097dd2a66b8a41414f66a1dd")
        },
        {
            "_id": ObjectId("f89745a672dcabf79c221f17"),
            "username": "Karen.Gonzalez463",
            "first_name": "Karen",
            "last_name": "Gonzalez",
            "email": "Karen.Gonzalez463@company.com",
            "password": "70NT15ARNWCR860",
            "favorites": 1081,
            "followers": 2317,
            "following": 7857,
            "created": datetime.datetime.strptime("2012-11-23", "%Y-%m-%d"),
            "personnel": 'admin2',
            "deletion_date": datetime.datetime.strptime("2022-11-23", "%Y-%m-%d"),
            "old_id": ObjectId("c979acd1caa94f9cd6967abc")
        }
    ]
)

# Print the number of documents inserted
print(f"{len(result.inserted_ids)} documents were inserted into the 'TRASHCAN' collection.")