require( './db' );
var express = require( 'express' );
var routes  = require( './routes' );
var fs = require('fs')
var path    = require( 'path' );
var app     = express();
var http    = require( 'http' ).createServer( app );
var engine  = require( 'ejs-locals' );
var io = require('socket.io')(http);
const exec = require('child_process').exec;
var mongoose = require( 'mongoose' );
var Todo     = mongoose.model( 'Todo' );
 
// all environments
app.set( 'port', process.env.PORT || 3001 );
app.engine( 'ejs', engine );
app.set( 'views', path.join( __dirname, 'views' ));
app.set( 'view engine', 'ejs' );
app.use( express.favicon());
app.use( express.logger( 'dev' ));
app.use( express.json());
app.use( express.bodyParser());
app.use( express.urlencoded());
app.use( express.methodOverride());
app.use( app.router );
app.use( express.static( path.join( __dirname, 'public' )));
 
app.get( '/', routes.index );
app.post( '/create', routes.create );
app.get( '/result', routes.result );


io.on('connection', function(socket){
	console.log('connection!!');
	socket.on('cal', function(msg){
		console.log('grading')
		console.log(msg)

		fs.writeFile("a.py", msg, function (err) {
  			if (err) {
    			return console.log(err);
  			}
  			console.log("save success!!");
		});
		exec('python eval.py', function(err, stdout, stderr){
			console.log('hh')
			if(err != null){
				console.log('exec fail@@')
			}
			console.log('result: '+ stdout);
			console.log('err: '+ stderr);
			new Todo({
    			content    : stdout,
    			updated_at : Date.now()
  			}).save();
		});
		
	});
});
 
http.listen( app.get( 'port' ), function(){
  console.log( 'Express server listening on port ' + app.get( 'port' ));
} );
