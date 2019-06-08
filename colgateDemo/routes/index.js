var express = require('express');
var router = express.Router();

var MongoClient = require('mongodb').MongoClient;



/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'colgate hi' ,message: ''});
});

router.get('/signup', function(req, res, next) {
  res.render('create_account');
});

router.post('/create', function(req, res, next) {
    var account = req.body.username;
    var password = req.body.password;
    MongoClient.connect("mongodb://localhost:27017", function(err, db) {
        if (err) throw err;
        //Write databse Insert/Update/Query code here..
        console.log('mongodb is running!');
        const mydb = db.db('testDB');
        mydb.collection('Persons', function(err, collection) {
            collection.insertOne({ Name: account, Password: password });
            collection.count(function(err, count) {
                if (err) throw err;
                console.log('Total Rows:' + count);
            });
        });

        db.close();
    });
    res.render('index', { title: 'colgate hi', message: '' });
});

router.post('/login', function(req, res, next) {
    var account = req.body.username;
    var password = req.body.password;
    console.log("name : " + account + " password : " + password);
    MongoClient.connect("mongodb://localhost:27017", function(err, db) {
        if (err) throw err;
        //Write databse Insert/Update/Query code here..
        console.log('mongodb is running!');
        const mydb = db.db('testDB');
        mydb.collection("Persons", function(err, collection) {
            collection.find({ Name: account , Password: password}).toArray(function(err, items) {
                if (items.length === 0) res.render('index',{title: 'colgate hi', message: 'your account is not exist or your password is incorrect'});
                else res.render('success', { title: 'success' });
                console.log(items.length)
            });
        });

        db.close();
    });

});
module.exports = router;
