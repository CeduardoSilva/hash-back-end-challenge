var dbName = "TestDB";
var MongoClient = require('mongodb').MongoClient;
var url = `mongodb://localhost:27017/${dbName}`;

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