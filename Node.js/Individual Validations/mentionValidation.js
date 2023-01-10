const ObjectId = require('bson').ObjectId;


const mentionVal = {
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

module.exports = { mentionVal };