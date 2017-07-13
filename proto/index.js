var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var port = process.env.PORT || 8000;
var fs = require('fs')
const exec = require('child_process').exec;


app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

app.get("/result", function(req,res) {
    res.sendFile(__dirname + "/result.html");
});

io.on('connection', function(socket){
  //console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  socket.on('submit', function(msg){
    console.log('code: ' + msg);
    fs.writeFile("a.py", msg, function (err) {
  		if (err) {
    		return console.log(err);
  		}
  		console.log("save success!!");
	});
	/*fs.readFile('/etc/hosts', 'utf8', function (err,data) {
  		if (err) {
    		return console.log(err);
  		}
  		console.log(data);
	});*/
	exec('python a.py', function(err, stdout, stderr){
		if(err != null){
			console.log('exec fail@@')
		}
		console.log('stdout: '+ stdout);

		fs.writeFile("a.out", stdout, function (err) {
  			if (err) {
    			return console.log(err);
  			}
  			console.log("save output success!!");
		});
	});
	setTimeout(function(){
		console.log("stop")
	}, 3000);
    io.emit('chat message', msg);
  });
});


http.listen(8000, function(){
	console.log('listening on *:8000');
});