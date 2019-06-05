var express = require('express');
var request = require('request-promise-native');

var app = express();

app.get("/", function(req, res) {
  console.log("Get started");
  request.get("http://api:8080/info").then((data) => {
    res.send('api response: ' + data);
  }).catch((err) => {
    res.send('Error API '+ err + '\n');
  });
})

app.listen(3000, () => {
  console.log("Listening on 3000...")
});
