var mongoose = require( 'mongoose' );
var Todo     = mongoose.model( 'Todo' );

exports.index = function ( req, res ){
  Todo.find( function ( err, todos, count ){
    res.render( 'index', {
        title : 'Python Online Judge System',
        todos : todos
    });
  });
};

exports.create = function ( req, res ){
  new Todo({
    content    : req.body.content,
    updated_at : Date.now()
  }).save( function( err, todo, count ){
    res.redirect( '/' );
  });
};

function sleep(time, callback) {
    var stop = new Date().getTime();
    while(new Date().getTime() < stop + time) {
        ;
    }
    callback();
}

exports.result = function ( req, res ){
  sleep(0, function() {
   // executes after one second, and blocks the thread
  });
  Todo.findOne({}, {}, { sort: { 'updated_at' : -1 } },( function ( err, todos ){
    res.render( 'edit', {
        title   : 'Result',
        todos   : todos,
        current : req.params.id
    });
  }));
};