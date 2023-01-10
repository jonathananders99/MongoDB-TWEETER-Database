from pymongo import MongoClient

# Connects to online MongoDB cluster
client = MongoClient("mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority")


# Uses database TWEETER
db = client["TWEETER"]


# add a trash can collection to let all documents that are deleted from other collections over 30 days be deleted
db.create_collection("TRASHCAN", validator= 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['personnel', 'deletion_date', 'old_id'],
            "properties": {
                "personnel": {
                    "bsonType": ['string'],
                },
                "deletion_date": {
                    "bsonType": ['date'],
                },
                "old_id": {
                    "bsonType": ['objectId'],
                }
            }
        }
    }
)

# Create TWEET
db.create_collection("TWEET")
# Add Validations after its already been created
db.command( { "collMod": "TWEET", "validator": 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['user_id', 'tweet', 'favorites', 'replies', 
            'retweets', 'mentions', 'tags', 'creation_date', 'edit_date'],
            "properties": {
                "user_id": {
                    "bsonType": ['objectId'],
                },
                "tweet": {
                    "bsonType": ['string'],
                },
                "favorites": {
                    "bsonType": ['array'],
                },
                "replies": {
                    "bsonType": ['array'],
                },
                "retweets": {
                    "bsonType": ['array'],
                },
                "mentions": {
                    "bsonType": ['array'],
                },
                "tags": {
                    "bsonType": ['array'],
                },
                "creation_date": {
                    "bsonType": ['date'],
                },
                "edit_date": {
                    "bsonType": ['date', 'null'],
                },
            },
        }
    }
})

#create USER with validations
db.create_collection("USER", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['username', 'first_name', 'last_name', 'email', 
                'password', 'favorites', 'followers', 'following', 'created'],
            "properties": {
                "username": {
                    "bsonType": ['string'],
                },
                "first_name": {
                    "bsonType": ['string'],
                },
                "last_name": {
                    "bsonType": ['string'],
                },
                "email": {
                    "bsonType": ['string'],
                },
                "password": {
                    "bsonType": ['string'],
                },
                "favorites": {
                    "bsonType": ['int'],
                    "minimum": 0,
                },
                "followers": {
                    "bsonType": ['int'],
                    "minimum": 0,
                },
                "following": {
                    "bsonType": ['int'],
                    "minimum": 0,
                },
                "created": {
                    "bsonType": ['date'],
                }
            }
        }
    }
)

# Create TAG with Validations
db.create_collection("TAG", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['name', 'tweets', 'creation_date'],
            "properties": {
                "name": {
                    "bsonType": ['string'],
                },
                "tweets": {
                    "bsonType": ['int'],
                },
                "creation_date": {
                    "bsonType": ['date'],
                }
            }
        }
    }
)

# Create TAGGING with Validations
db.create_collection("TAGGING", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['tag_id', 'tweet_id', 'date_tagged'],
            "properties": {
                "tag_id": {
                    "bsonType": ['objectId'],
                },
                "tweet_id": {
                    "bsonType": ['objectId'],
                },
                "date_tagged": {
                    "bsonType": ['date'],
                }
            }
        }
    }
)

# Create RETWEET with Validations
db.create_collection("RETWEET", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['tweet_id', 'retweet_id'],
            "properties": {
                "tweet_id": {
                    "bsonType": ['objectId'],
                },
                "retweet_id": {
                    "bsonType": ['objectId'],
                }
            }
        }
    }
)

# Create FOLLOWER with Validations
db.create_collection("FOLLOWER", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['user_id', 'follower_id', 'date_followed'],
            "properties": {
                "user_id": {
                    "bsonType": ['objectId'],
                },
                "follower_id": {
                    "bsonType": ['objectId'],
                },
                "date_followed": {
                    "bsonType": ['date'],
                }
            }
        }
    }
)

# Create FAVORITE with Validations
db.create_collection("FAVORITE", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['tweet_id', 'user_id', 'date_favorited'],
            "properties": {
                "tweet_id": {
                    "bsonType": ['objectId'],
                },
                "user_id": {
                    "bsonType": ['objectId'],
                },
                "date_favorited": {
                    "bsonType": ['date'],
                }
            }
        }
    }
)

# Create REPLY with Validations
db.create_collection("REPLY", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['tweet_id', 'user_id', 'reply', 'date_replied', 'date_updated'],
            "properties": {
                "tweet_id": {
                    "bsonType": ['objectId'],
                },
                "user_id": {
                    "bsonType": ['objectId'],
                },
                "reply": {
                    "bsonType": ['string'],
                },
                "date_replied": {
                    "bsonType": ['date'],
                },
                "date_updated": {
                    "bsonType": ['date', 'null'],
                }
            }
        }
    }
)

# Create MENTION with Validations
db.create_collection("MENTION", validator = 
    {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": ['tweet_id', 'user_id', 'date_mentioned'],
            "properties": {
                "tweet_id": {
                    "bsonType": ['objectId'],
                },
                "user_id": {
                    "bsonType": ['objectId'],
                },
                "date_mentioned": {
                    "bsonType": ['date'],
                }
            }
        }
    }
)