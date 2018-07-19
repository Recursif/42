
var exec = require("child_process").exec

exec('node test-program', (err, stdout, stderr) => {
    console.log(stdout)
})