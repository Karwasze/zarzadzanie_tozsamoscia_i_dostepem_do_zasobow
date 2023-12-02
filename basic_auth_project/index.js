const express = require("express");
var path = require('path');

const app = express();

function authentication(req, res, next) {
    // sprawdzamy czy istnieją headery "authorization"
    var authheader = req.headers.authorization;
    console.log(req.headers);
    // jeśli ich nie ma to nie zezwalamy na dostęp
    if (!authheader) {
        var err = new Error('You are not authenticated!');
        res.setHeader('WWW-Authenticate', 'Basic');
        err.status = 401;
        return next(err)
    }
    // wyciągamy hash usera i hasła z headera
    var auth = new Buffer.from(authheader.split(' ')[1],
        'base64').toString().split(':');
    var user = auth[0];
    var pass = auth[1];
    // sprawdzamy czy user i hasło są poprawne
    if (user == '' && pass == '') {

        // If Authorized user
        next();
    } else {
        // jeśli nie jest to nie zezwalamy na dostęp
        var err = new Error('You are not authenticated!');
        res.setHeader('WWW-Authenticate', 'Basic');
        err.status = 401;
        return next(err);
    }

}

// First step is the authentication of the client
app.use(authentication)
app.use(express.static(path.join(__dirname, 'public')));

// Server setup
app.listen((3000), () => {
    console.log("Server is Running");
})