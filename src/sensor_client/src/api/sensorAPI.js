export function testAPI(setState) {
    console.log('hit testAPI()')

    fetch("/getLogs").then(res => res.text()).then(res => setState(JSON.parse(res)));
        // .then(res => res
        //     console.log('*** after Text is: ' + res);
        //     retval = res
        // });

}