const { MongoClient } = require('mongodb');
const docs = ['favorite', 'follower', 'mention', 'reply', 'retweet', 'tag', 'tagging', 'trashcan', 'tweet', 'user'].reduce((acc, cur) => {
    acc[`${cur}Docs`] = require(`./Individual Documents/${cur}Documents`)[`${cur}Docs`];
    return acc;
  }, {});


async function connectToDatabase() {
    const uri = "mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority";
    const client = new MongoClient(uri);
    try {
        // Connect cluster
        await client.connect();
        // Run operations
        await operations(client);
    } catch (e) {
        console.error(e);
    } finally {
        // Close connection
        await client.close();
    }
}



async function operations(client) {
    const db = await client.db("TWEETER");
    
    
    // Insert the documents into the FAVORITE collection
    await insertDocs(db, docs.favoriteDocs, "FAVORITE")

    // Insert the documents into the FOLLOWER collection
    await insertDocs(db, docs.followerDocs, "FOLLOWER")

    // Insert the documents into the MENTION collection
    await insertDocs(db, docs.mentionDocs, "MENTION")

    // Insert the documents into the REPLY collection
    await insertDocs(db, docs.replyDocs, "REPLY")

    // Insert the documents into the RETWEET collection
    await insertDocs(db, docs.retweetDocs, "RETWEET")

    // Insert the documents into the TAG collection
    await insertDocs(db, docs.tagDocs, "TAG")

    // Insert the documents into the TAGGING collection
    await insertDocs(db, docs.taggingDocs, "TAGGING")

    // Insert the documents into the TRASHCAN collection
    await insertDocs(db, docs.trashcanDocs, "TRASHCAN")

    // Insert the documents into the TWEET collection
    await insertDocs(db, docs.tweetDocs, "TWEET")

    // Insert the documents into the USER collection
    await insertDocs(db, docs.userDocs, "USER")
};

async function insertDocs(db, curDocs, collectionName) {
    const collection = db.collection(collectionName);
    const result = await collection.insertMany(curDocs);
    console.log(`${result.insertedCount} documents were inserted into the ${collectionName} collection.`);
}

connectToDatabase().catch(console.error);

