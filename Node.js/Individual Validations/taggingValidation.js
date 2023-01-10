const ObjectId = require('bson').ObjectId;


const taggingVal = {
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

module.exports = { taggingVal };