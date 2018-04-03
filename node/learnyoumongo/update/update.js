const mongo = require('mongodb').MongoClient

const url = 'mongodb://localhost:27017/' + process.argv[2]

mongo.connect(url, fonction(err, db) {
	if (err) console.log(err)
	
	const users = db.collection('users')
	
	users.update({
		username: 'tinatime'
	}, {
		$set: {
			age: 40
		}
	}, function(err) {
		if (err) console.log(err)
		db.close()
	})
})

