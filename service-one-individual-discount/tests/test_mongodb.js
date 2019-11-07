// Test Mongo DB

var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://localhost/TestCollection';

MongoClient.connect(url, function(err, db) {
    console.log("Connected");
    db.collection('TestCollection').insertOne({
        Employeeid: 13,
        EmployeeName: "NewEmployee"
    }).then(() => {
        var cursor = db.collection('TestCollection').find();
        cursor.each(function(err,doc) {
            console.log(doc);
        });
        db.collection('TestCollection').updateOne({
            "Employeeid": 13
        }, {
            $set: {
                "EmployeeName": "ANTEDEGUEMON"
            }
        }).then(() => {
            var cursor = db.collection('TestCollection').find();
            cursor.each(function(err,doc) {
                console.log(doc);
            });
            db.collection('TestCollection').deleteOne(
                {
                    "EmployeeName": "ANTEDEGUEMON"
                }
            ).then(() => {
                var cursor = db.collection('TestCollection').find();
                cursor.each(function(err,doc) {
                    console.log(doc);
                });
            });
        });
    });
});