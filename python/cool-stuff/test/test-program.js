
async function test() {
    for (var i = 0; i < 50; i++) {
        await new Promise(() => setTimeout(() => {
            console.log("ok") 
        }, 5000));
    }
}

test()

