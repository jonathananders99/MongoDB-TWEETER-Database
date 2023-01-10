const ObjectId = require('bson').ObjectId;


const favoriteVal = {
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

module.exports = { favoriteVal };