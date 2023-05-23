import React from "react"
import ReactDOM from "react-dom"
import StAudioRec from "./StreamlitAudioRecorder"

import Audio from "./Audio"
// import Test from "./Test"
ReactDOM.render(
  <React.StrictMode>
    <StAudioRec />
    {/* <Test /> */}
    {/* <Audio/> */}
  </React.StrictMode>,
  document.getElementById("root")
)
