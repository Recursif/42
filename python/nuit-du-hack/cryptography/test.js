const http = require('http')

var server = http.createServer(function(req, res) {
	var rawData = '';
	res.on('data', (data) => {
		rawData += data.toString();
		console.log(data);
	});
	res.end("end"); 
});

server.on('listening', () => {
	console.log("Serveur web lancé sur localhost:5555 ...");
});
server.listen(5555);
