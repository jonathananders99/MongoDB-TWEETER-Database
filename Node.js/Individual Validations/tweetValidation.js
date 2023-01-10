const ObjectId = require('bson').ObjectId;


const tweetVal = {
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

module.exports = { tweetVal };