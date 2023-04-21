import { React, useState } from 'react'
import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"

const Audio = () => {
  const [isFocused, setIsFocused] = useState(false);
  const [recordState, setRecordState] = useState(null);
  const [audioDataURL, setAudioDataURL] = useState('');
  const [reset, setReset] = useState(false);
  const [regis, setRegis] = useState(false);


  const onStop_audio = (data) => {
    if (reset === true) {
      setAudioDataURL('')
    } else {
      setAudioDataURL(data.url)
    }

    // fetch(data.url).then((ctx) => {
    //   return ctx.blob()
    // })

  }

  const startRecord = (e) => {
    // 버튼을 클릭했을 때 mqtt 연동 가능토록 해야 함
    // 이는 python에서 처리. 버튼 클릭이 trigger가 되고 파이썬 코드가 실행되도록
    // 이 코드에서 document.querySelector를 사용해서 streamlit으로 만든 위젯에 접근 가능한지 확인 필요
    // 가능하다면 hidden으로 만든 버튼을 클릭하게 동작
    // 해당 버튼 클릭 시 mqtt, wss 전송 등 가능토록 코드를 작성
    if (e.target.innerText === '녹음') {
      setReset(false)
      setAudioDataURL('');
      setRecordState(RecordState.START)
      console.log(RecordState.START)
      // Streamlit.setComponentValue('')
      e.target.innerText = '중지'
      e.target.id = 'stop'
      
    } else {
      setReset(false)
      setAudioDataURL('');
      setRecordState(RecordState.STOP)
    
      e.target.innerText = '녹음'
      e.target.id = 'record'
    }
  }
  return (
    <div>
      Audio
      <AudioReactRecorder
        state={recordState}
        onStop={onStop_audio}
        type='audio/wav'
        backgroundColor='rgb(255, 255, 255)'
        foregroundColor='rgb(255,76,75)'
        canvasWidth={''}
        canvasHeight={39}
      ></AudioReactRecorder>
      <button onClick={startRecord}>녹음</button>
    </div>
  )
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(Audio)
// export default StAudioRec

// Tell Streamlit we're ready to start receiving data. We won't get our
// first RENDER_EVENT until we call this function.
Streamlit.setComponentReady()

// Finally, tell Streamlit to update our initial height. We omit the
// `height` parameter here to have it default to our scrollHeight.
Streamlit.setFrameHeight()
