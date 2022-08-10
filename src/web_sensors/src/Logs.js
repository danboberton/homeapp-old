import { log } from './logs/symLog.log'

function Logs(){
    let logName = "2022-08-09-105303.log"
    let logDir = "../../logs/"
    let retval

    fetch('./logs/symLog.log').then((response => response.text()
        .then((data) => {
            retval = data
            console.log(data)
            console.log("endData")
        })))
    return(
        <div className="Logs">
            <p>Result {retval}</p>
        </div>
    );
}

export default Logs;