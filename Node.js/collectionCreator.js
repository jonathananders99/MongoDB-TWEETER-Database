const { MongoClient } = require('mongodb');
const validators = ['favorite', 'follower', 'mention', 'reply', 'retweet', 'tag', 'tagging', 'trashcan', 'tweet', 'user'].reduce((acc, cur) => {
    acc[`${cur}Val`] = require(`./Individual Validations/${cur}Validation`)[`${cur}Val`];
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
    
    // add a trash can collection to let all documents that are deleted from other collections over 30 days be deleted
    await db.createCollection("TRASHCAN", { validator: validators.trashcanVal});

    // Create TWEET
    await db.createCollection("TWEET");
    // Add Validations after its already been created
    await db.command( { "collMod": "TWEET", "validator": validators.tweetVal});

    // Create USER with validations
    await db.createCollection("USER", { validator: validators.userVal});
    
    // Create TAG with Validations
    await db.createCollection("TAG", { validator: validators.tagVal});

    // Create TAGGING with Validations
    await db.createCollection("TAGGING", { validator: validators.taggingVal});

    // Create RETWEET with Validations
    await db.createCollection("RETWEET", { validator: validators.retweetVal});

    // Create FOLLOWER with Validations
    await db.createCollection("FOLLOWER", { validator: validators.followerVal});

    //Create FAVORITE with Validations
    await db.createCollection("FAVORITE", { validator: validators.favoriteVal});
    
    // Create REPLY with Validations
    await db.createCollection("REPLY", { validator: validators.replyVal});
    
    // Create MENTION with Validations
    await db.createCollection("MENTION", { validator: validators.mentionVal});
};


connectToDatabase().catch(console.error);