import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import 'audio-react-recorder/dist/index.css'


interface State {
  isFocused: boolean
  recordState: null
  audioDataURL: string
  reset: boolean
  regis: boolean
}

class StAudioRec extends StreamlitComponentBase<State> {
  public state = {
    isFocused: false, recordState: null,
    audioDataURL: '', reset: false,
    regis: false
  }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    const { theme } = this.props
    const style: React.CSSProperties = {}

    const { recordState } = this.state

    // compatibility with older vers of Streamlit that don't send theme object.
    if (theme) {
      // Use the theme object to style our button border. Alternatively, the
      // theme style is defined in CSS vars.
      const borderStyling = `1px solid ${this.state.isFocused ? theme.primaryColor : "gray"}`
      style.border = borderStyling
      style.outline = borderStyling
    }

    return (
      <>
        <span>
          <div className="audio_rec_cover">
            <div className="audio_canvas">
              <AudioReactRecorder
                state={recordState}
                onStop={this.onStop_audio}
                type='audio/wav'
                backgroundColor='rgb(255, 255, 255)'
                foregroundColor='rgb(255,76,75)'
                canvasWidth={''}
                canvasHeight={39}

              />
            </div>
            <div>
              <button id='record' onClick={this.onClick_start}>
                녹음
              </button>
            </div>
          </div>
          {/* <br></br> */}
          {/* <button id='stop' onClick={this.onClick_stop}
            style={{display:'none'}}
          >
            Stop
          </button> */}
          {/* <button id='reset' onClick={this.onClick_reset}>
            Reset
          </button>

          <button id='continue' onClick={this.onClick_continue}>
            Download
          </button> */}

          {/* <AudioReactRecorder
            state={recordState}
            onStop={this.onStop_audio}
            type='audio/wav'
            backgroundColor='rgb(255, 255, 255)'
            foregroundColor='rgb(255,76,75)'
            canvasWidth={165}
            canvasHeight={40}
          /> */}
          <div className="audio_player">
            <audio
              id='audio'
              controls
              src={this.state.audioDataURL}
            />
            {/* {
            this.state.regis
              ?
              <button id='record' 
                style={{float: "right", marginRight:"0"}}
                onClick={this.onClick_continue}
                >등록</button>
              :
              <></>
            } */}
          </div>
          
        </span>
      </>
    )
  }


  private onClick_start = (e) => {
    if (e.target.innerText === '녹음') {
      this.setState({
        reset: false,
        audioDataURL: '',
        recordState: RecordState.START
      })
      Streamlit.setComponentValue('')
      e.target.innerText = '중지'
      e.target.id = 'stop'
      return true
    } else {
      this.setState({
        reset: false,
        recordState: RecordState.STOP,
        regis: true
      })
      e.target.innerText = '녹음'
      e.target.id = 'record'
    }
    // console.log(e)
  }

  private onClick_regis = (e) => {

  }

  // private onClick_stop = () => {
  //   this.setState({
  //     reset: false,
  //     recordState: RecordState.STOP
  //   })
  // }

  private onClick_reset = () => {
    this.setState({
      reset: true,
      audioDataURL: '',
      recordState: RecordState.STOP
    })
    Streamlit.setComponentValue('')
  }

  private onClick_continue = () => {
    if (this.state.audioDataURL !== '') {
      // get datetime string for filename
      let datetime = new Date().toLocaleString();
      datetime = datetime.replace(' ', '');
      datetime = datetime.replace(/_/g, '');
      datetime = datetime.replace(',', '');
      var filename = 'streamlit_audio_' + datetime + '.wav';

      // auromatically trigger download
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = this.state.audioDataURL;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
    }
  }

  private onStop_audio = (data) => {
    if (this.state.reset === true) {
      this.setState({
        audioDataURL: ''
      })
      Streamlit.setComponentValue('')
    } else {
      this.setState({
        audioDataURL: data.url
      })

      fetch(data.url).then(function (ctx) {
        return ctx.blob()
      }).then(function (blob) {
        // converting blob to arrayBuffer, this process step needs to be be improved
        // this operation's time complexity scales exponentially with audio length
        return (new Response(blob)).arrayBuffer()
      }).then(function (buffer) {
        Streamlit.setComponentValue({
          "arr": new Uint8Array(buffer)
        })
      })

    }


  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(StAudioRec)
// export default StAudioRec

// Tell Streamlit we're ready to start receiving data. We won't get our
// first RENDER_EVENT until we call this function.
Streamlit.setComponentReady()

// Finally, tell Streamlit to update our initial height. We omit the
// `height` parameter here to have it default to our scrollHeight.
Streamlit.setFrameHeight()
