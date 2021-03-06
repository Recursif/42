
// Load basic module for file system path and https server
const fs = require('fs')
const path = require('path')
const https = require('https')

// Load express and instanciate it
const express = require('express')
const app = express()


const bodyParser = require('body-parser')

// Load mongoose the elegant mongodb object modeling for node.js
const mongoose = require('mongoose')

// Load env variables
//const env = require('dotenv').config()

const Channel = require('./models/Channel')


// Controllers 
const channelController = require('./controllers/channel')



var webpack = require('webpack')
var webpackConfig = require('../webpack.config')()
var compiler = webpack(webpackConfig)



mongoose.connect('mongodb://localhost:27017/chat')
mongoose.connection.on("error", () => {
    console.log('MongoDB Connection Error. Please make sure that MongoDB is running!')
    process.exit(1)
})


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))


if (app.get('env') === 'development') {
    app.use(require('webpack-dev-middleware')(compiler, {
      noInfo: true,
      publicPath: webpackConfig.output.publicPath
    }));
    app.use(require('webpack-hot-middleware')(compiler))
}


// Static serve the express repository
app.use(express.static(path.join(__dirname, 'dist')))


//-- Get methods --

app.get('/channel', channelController.getChannels)

app.post('/channel/add', channelController.addChannel)


// Route to access to the landing page
app.get('/*', (req, res) => {
    res.sendFile(path.join(__dirname, '../dist/index.html'))
    //__dirname : It will resolve to your project folder.
})



app.listen(8080)

module.exports = app
