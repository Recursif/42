
module.exports = () => {
    console.log(process.env.NODE_ENV)
    switch (process.env.NODE_ENV) {
        case "production":
            console.log("Load webpack config from PRODUCTION build...\n")
            return require('./config/webpack.prod.config.js')
        case "development":
            console.log("Load webpack config from PRODUCTION build...\n")
            return require('./config/webpack.dev.config.js')
        case "server":
            console.log("Load webpack config from SERVER build...\n")
            return require('./config/webpack.server.config.js')
        default:
            console.log("No NODE_ENV specified. Exiting...")
            return
    }
}