export function getLogs(setState) {
    console.log('hit testAPI()')

    fetch("/getLogs").then(res => res.text()).then(res => setState(JSON.parse(res)));
        // .then(res => res
        //     console.log('*** after Text is: ' + res);
        //     retval = res
        // });

}

export function getLog(e) {
    console.log('hit testAPI()')

    fetch("/getLogs").then(res => res.text()).then(res => e = res);
    // .then(res => res
    //     console.log('*** after Text is: ' + res);
    //     retval = res
    // });

}