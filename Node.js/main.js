const { MongoClient, ObjectId } = require('mongodb');
const moment = require('moment-timezone');


async function connectToDatabase() {
    const uri = "mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority";

    try {
        // Connect to the cluster and perform the operations
        MongoClient.connect(uri, { useUnifiedTopology: true }, operations);
    } catch (e) {
        console.error(e);
    }
}


async function operations(err, client) {
    if (err) {
        console.error(err);
        return;
    }

    const db = client.db("TWEETER");
    
    // Get a list of the collections in the database
    const collections = await db.listCollections().toArray();
    // Iterate through the collections and print the name and validation rules
    collections.forEach(collection => {
        const name = collection.name;
        const options = collection.options;
        if (options.validator) {
            console.log(`Collection name: ${name}`);
            console.dir(options.validator, { depth: null });
        } else {
            console.log(`The '${name}' collection does not have any validation rules.`);
        }
    });

    // All users with above 5000 followers, only return usernames, and follower count. 
    // Sort by follower count, limit to 10 results
    let cursor = await db.collection("USER").find(
        {
            $and: [
                { followers: { $gt: 5000 } },
            ]
        },
        {
            _id: 0,
            username: 1,
            followers: 1
        }
    ).sort({ followers: -1 }).limit(10);
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // All replies from one user that were updated at least once, only return ids
    cursor = await db.collection("REPLY").find(
        {
            $and: [
                { user_id: ObjectId("60c714351b4f61adc8f6622f") },
                { date_updated: { $ne: null } },
            ],
        },
        {
            _id: 1,
        },
    );
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // All of a user's followers, returns only followers ids
    cursor = await db.collection("FOLLOWER").find(
        {
            $and: [
                { user_id: ObjectId("d635031a11e52d3b81688e6e") },
            ],
        },
        {
            follower_id: 1,
            _id: 0,
        },
    );
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });
    
    // All users with less than 7500 followers with more than 5000 favorites for 
    // users created from current date to 2020-12-10, return usernames
    cursor = await db.collection("USER").find(
        {
            $and: [
                { followers: { $lt: 7500 } },
                { favorites: { $gt: 5000 } },
                { created: { $gt: new Date("2020-12-10"), $lt: new Date() } },
            ],
        },
        {
            _id: 0,
            username: 1,
        },
    );
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // All tweets from last 5 years for one person
    cursor = await db.collection("TWEET").find(
        {
            $and: [
                { user_id: ObjectId("80629ffc3c0f4c28aa386662") },
                { creation_date: { $gt: new Date("2017-12-10"), $lt: new Date() } },
            ],
        },
    );
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // Which user has the most amount of tweets 
    cursor = await db.collection("TWEET").aggregate([
        { $sortByCount: "$user_id" },
        { $limit: 1 },
    ]);
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // Top 10 tweets with the most replies
    cursor = await db.collection("TWEET").aggregate([
        {
            $project: {
                replies_count: {
                    $size: {
                        $ifNull: ["$replies", []],
                    },
                },
            },
        },
        {
            $sort: { replies_count: -1 },
        },
        {
            $limit: 10,
        },
    ]);
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // All Tweets with 10 or more than favorites, return fav counts and ids, 
    // sort by fav count desc using $sort in pipeline
    cursor = await db.collection("TWEET").aggregate([
        {
            $project: {
                favorites_count: {
                    $size: {
                        $ifNull: ["$favorites", []],
                    },
                },
            },
        },
        {
            $match: { favorites_count: { $gte: 10 } },
        },
        {
            $sort: { favorites_count: -1 },
        },
    ]);
    // Iterate through the cursor and print the documents
    cursor.forEach((doc) => {
        console.log(doc);
    });

    // imitates a trigger for an on deletion of a document in TWEET collection
    // move a tweet meant for deletion to the trashcan after necessary modification and delete it from tweet collection
    tweetTrash(new ObjectId("4aad42147a8f3e8ba32028fd"), db);

    // given the id of a user increase the follower count by one
    incFollower(new ObjectId("d635031a11e52d3b81688e6e"), db);

    // given the id of a user increase the follower count by one
    incFollowing(new ObjectId("d635031a11e52d3b81688e6e"), db);

    // imitates a trigger for an insert into FOLLOWER
    insertIntoFollower({
        _id: ObjectId('ba9c74bcd388d8cc66d03904'),
        user_id: ObjectId('018ea6a44222d47078ba8334'),
        follower_id: ObjectId('c1511c0be859be2b841f9901'),
        date_followed: new Date('2009-02-15'),
    }, db);
    
    // deletes any document in TRASHCAN with a deletion date of over 30 days ago or older.
    trashDelete30Days(db);
}


async function tweetTrash(curId, db) {
    try {
        // Get the first document from the cursor
        const tweet = await db.collection('TWEET').aggregate([
            {
                $match: {_id: curId}
            },
            {
                $addFields: {
                    _id: new ObjectId(),
                    personnel: 'admin1',
                    deletion_date: new Date(),
                    old_id: curId,
                },
            },
        ]).next();

        // Insert the modified document into the "TRASHCAN" collection
        await db.collection('TRASHCAN').insertOne(tweet);

        // Delete the document from the "TWEET" collection
        await db.collection('TWEET').deleteOne({ _id: curId });
        console.log('Tweet has been moved to trashcan');

    } catch (error) {
        console.error(error);
    }
}


async function incFollower(curId, db) {
    try {
        // increment follower count by one
        await db.collection('USER').updateOne(
            {_id: curId},
            {$inc: {followers: 1}}
        );
        console.log(`Follower count incremented by 1 for document with id: ${curId}`);
    } catch (error) {
        console.error(error);
    }
}


async function incFollowing(curId, db) {
    try {
        // increment following count by one
        await db.collection('USER').updateOne(
            {_id: curId},
            {$inc: {following: 1}}
        );
        console.log(`Following count incremented by 1 for document with id: ${curId}`);
    } catch (error) {
        console.error(error);
    }
}


async function insertIntoFollower(doc, db) {
    try {
        // inserts document
        await db.collection('FOLLOWER').insertOne(doc);
        console.log(`Document with id: ${doc._id} inserted into FOLLOWER collection`);
        // increment follower count
        incFollower(doc.user_id, db);
        // increment following count
        incFollowing(doc.follower_id, db);
    } catch (error) {
        console.error(error);
    }
}


async function trashDelete30Days(db) {
    try {
        const delCount = await db.collection('TRASHCAN').deleteMany({
            deletion_date: {
                $lte: new Date(Date.now() - moment.duration(30, 'days')),
            },
        });
        console.log(`${delCount.deletedCount} documents deleted from the trashcan`);
    } catch (error) {
        console.error(error);
    }
}


// runs program
connectToDatabase().catch(console.error);