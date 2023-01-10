### This version is in ***Javascript*** using ***NodeJS***

### Description:
This portion is split into multiple files:
- *CollectionCreation* where the collections are created with validations.
- *Main* where functions, triggers, table updates, queries, and more are.
- *AllDocuments* file where the data is inserted. Each collection is stored in the *Individual Documents* folder and is called by allDocuments file instead of having each collection in the file making the size very large.

### How to Run:
1. You will need to change the URI in each file to either an existing cluster or a local cluster
2. Run the `collectionCreation` file
3. Run the `allDocuments` file
4. Run the `main` file