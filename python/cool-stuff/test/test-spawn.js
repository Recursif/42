
const { spawn } = require('child_process');

try {
    wait = spawn('python3', ['wait.py', 'lol']);
} catch (err) {
    console.log(err);
}


wait.stdout.on('data', (data) => {
    console.log(data.toString());
});
  
wait.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
});

wait.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});