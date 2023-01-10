const ObjectId = require('bson').ObjectId;


const tagVal = {
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

module.exports = { tagVal };