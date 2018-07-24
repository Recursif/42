var exec = require("child_process").exec
var crontab = require("node-crontab")


var job = crontab.scheduleJob("*/1 * * * *", () => {
    console.log("go!")
    exec('python3 wait.py', (err, stdout, stderr) => {
        console.log(stdout)
    })  
})

