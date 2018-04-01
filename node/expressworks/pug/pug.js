const path = require('path')
const express = require('express')
const app = express()
const pug = require('pug')


app.use(express.static(process.argv[3]))
app.set('view engine', pug)

app.set('views', path.join(__dirname, 'templates'))

app.get('/home', function(req, res) {
	res.render('index', {date: new Date().toDateString()})
})
app.listen(process.argv[2])

