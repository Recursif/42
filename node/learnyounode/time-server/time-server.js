var net = require('net');

var server = net.createServer(function (socket) {
	var date = new Date();
	var year = date.getFullYear();
	var month = date.getMonth();
	var day = date.getDate();
	var hours =date.getHours();
	var mins = date.getMinutes();
	var timestamp = year + '-' + month + '-' + day + ' ' + hours + ':' + mins;
	socket.write(timestamp);
})
server.listen(8000)
