var net = require('net');

var server = net.createServer(function(socket) {
	console.log('ok');
});


server.listen(5555);
