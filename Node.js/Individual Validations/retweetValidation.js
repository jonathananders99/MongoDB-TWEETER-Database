const ObjectId = require('bson').ObjectId;


const retweetVal = {
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

module.exports = { retweetVal };