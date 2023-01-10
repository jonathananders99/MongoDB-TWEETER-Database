const ObjectId = require('bson').ObjectId;


const userVal = {
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

module.exports = { userVal };