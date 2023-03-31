import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import 'audio-react-recorder/dist/index.css'

const Test = () => {
  const changeAttr = (e) => {
    console.log(e)
  }
  return (
    <div>
      <button
        onClick={changeAttr}
      >
        start
      </button>
      <button
        style={{display:'none'}}
        onClick={changeAttr}
      >
        stop
      </button>
    </div>
  )
}

export default Test;