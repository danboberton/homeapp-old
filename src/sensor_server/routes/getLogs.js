const express = require('express');
const router = express.Router();
const path = require('path');
const fs = require('fs');
const {log} = require("debug");

router.get('/', function(req, res, next) {
    let pwd = __dirname;
    let sub1 = pwd.lastIndexOf('/');
    pwd = pwd.slice(0, sub1);
    sub1 = pwd.lastIndexOf('/');
    pwd = pwd.slice(0, sub1);
    let logDir = path.join(pwd, '/logs');

    fs.readdir(logDir, function (err, files) {
        //handling error
        if (err) {
            return console.log('Unable to scan directory: ' + err);
        }
        //listing all files using forEach
        const result = {}
        for (const s of files){

        }
        res.send(JSON.stringify(files));
    });
});
module.exports = router;