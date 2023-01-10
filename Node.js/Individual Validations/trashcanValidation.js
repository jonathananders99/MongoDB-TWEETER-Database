const ObjectId = require('bson').ObjectId;


const trashcanVal = {
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

module.exports = { trashcanVal };