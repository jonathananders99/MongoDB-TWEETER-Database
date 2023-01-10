const ObjectId = require('bson').ObjectId;


const replyVal = {
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

module.exports = { replyVal };