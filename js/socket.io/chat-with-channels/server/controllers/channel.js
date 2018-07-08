
const Channel = require('../models/Channel')



/**
 * GET /channel
 * Controller to get a channel
 * 
 * @return channels the list of all the channels
 */
exports.getChannels = (req, res, next) => {

    // Find all channels
    Channel.find({}).exec((err, channels) => {
        if (err) {
            console.log("err:")
            console.log(err)
            return res.status(401).send({ msg: "Une erreur est survenue sur nos serveurs, veuillez nous contacter pour signaler un problème" })
        }
        res.send({ channels: channels })

    })
}


/**
 * POST /channel/add
 * Controller to add a channel
 * 
 * @param channelName
 * 
 * @return channel the edited channel
 */
exports.addChannel = (req, res, next) => {
    // Basic validations
    req.assert("channelName", "Le nom du channel ne peut pas être vide").notEmpty()
    console.log(req.body)
    
    var errors = req.validationErrors()

    if (errors) {
        return res.status(400).send(errors)
    }

    var channel = new Channel()

    channel.name = channelName

    channel.save((err) => {
        if (err) {
            console.log("err:")
            console.log(err)
            return res.status(401).send({ msg: "Une erreur est survenue sur nos serveurs, veuillez nous contacter pour signaler un problème" })
        }
        res.send({ channel: channel })
    })
}