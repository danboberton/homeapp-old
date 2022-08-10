import {useEffect, useState} from "react";
import {testAPI} from "../api/sensorAPI";
import ShowLog from "./ShowLog";

export default function LogList(){
    const [logs, setLogs] = useState(0)
    const [selFile, setSelFile] = useState(-1);

    const ctx = {logs, selFile}

    useEffect(() => {
        testAPI(setLogs);
    }, [])

    const liLogs = () => {
        if (logs){
            return logs.map((item, i) => {
                return (
                    <li key={i} onClick={() => setSelFile(i)}>{item}</li>
                )})
        }
    }

    return(

        <div className={'LogList'}>
            <ul>
                {liLogs()}
            </ul>
            <ShowLog props={ctx}/>
        </div>

    );
}