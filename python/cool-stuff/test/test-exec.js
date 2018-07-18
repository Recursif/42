
const exec = require("child_process").exec

exec('pwd', (err, stdout, stderr) => {
    console.log("lol")
    console.log(stdout)
})