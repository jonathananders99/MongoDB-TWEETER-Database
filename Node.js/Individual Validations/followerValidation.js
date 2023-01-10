const ObjectId = require('bson').ObjectId;


const followerVal = {
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

module.exports = { followerVal };