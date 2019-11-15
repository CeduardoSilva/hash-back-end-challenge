var dbName = "TestDB";
var MongoClient = require('mongodb').MongoClient;
var url = `mongodb://localhost:27017/${dbName}`;

/**
 * Creates a collection on the database with the name received
 * @param {String} collectionName 
 * @param {String} dbName 
 */
function createCollection(collectionName, dbName) {
    return new Promise((resolve, reject) => {
        MongoClient.connect(url, function(err, db) {
            if (err) throw reject(err);
            var dbo = db.db(dbName);
            dbo.createCollection(collectionName, function(err, res) {
              if (err) throw reject(err);
              db.close();
              resolve("Collection created!");      
            });
        });
    });
}

/**
 * Inserts a object into the collection and data base received
 * @param {Object} data 
 * @param {String} collectionName 
 * @param {String} dbName 
 */
function insert(data, collectionName, dbName) {
    return new Promise((resolve, reject) => {
        MongoClient.connect(url, function(err, db) {
            if (err) throw reject(err);
            var dbo = db.db(dbName);
            dbo.collection(collectionName).insertOne(data, function(err, res) {
              if (err) throw reject(err);
              db.close();
              resolve("1 document inserted");
            });
        });
    });
    
}

/**
 * Find a object from the collection and data base received using the query object
 * @param {Object} query 
 * @param {String} collectionName 
 * @param {String} dbName
 * @returns {Object} result 
 */
function findOne(query, collectionName, dbName) {
    return new Promise((resolve,reject) => {
        MongoClient.connect(url, function(err, db) {
            if (err) throw reject(err);
            var dbo = db.db(dbName);
            dbo.collection(collectionName).findOne(query, function(err, result) {
              if (err) throw reject(err);
              db.close();
              resolve(result);
            });
        });
    });
}

/**
 * Return all objects from the data base and collection received
 * @param {String} collectionName 
 * @param {String} dbName
 * @returns {Array} result
 */
function findAll(collectionName, dbName) {
    return new Promise((resolve, reject) => {
        MongoClient.connect(url, function(err, db) {
            if (err) throw reject(err);
            var dbo = db.db(dbName);
            dbo.collection(collectionName).find({}).toArray(function(err, result) {
              if (err) throw reject(err);
              db.close();
              resolve(result);
            });
        });
    });
}

module.exports = {
    createCollection: createCollection,
    insert: insert,
    findOne: findOne,
    findAll: findAll
}