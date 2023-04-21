import logo from './logo.svg';
import Audio from './compo/Audio';
// import StreamlitAudioRecorder_copy from './compo/StreamlitAudioRecorder_copy';

function App() {
  const changeAttr = (e) => {
    // console.log(e.target.style.display)
    console.log(e.target.innerText)
    e.target.id = 'test'
    console.log(e.target)
    // e.target.style.display = e.target.style.display !== "none" ? "none" : "block"
  }
  const test1 = (e) => {
    e.target.innerText = e.target.innerText === 'start' ? 'stop' : 'start'

    console.log(1);
  }
  const test2 = () => {
    console.log(2);
  }
  return (
    <div>
      <Audio></Audio>
      {/* <StreamlitAudioRecorder_copy></StreamlitAudioRecorder_copy> */}
      <button

        onClick={changeAttr}
        style={{ display: 'block' }}
      >
        start
      </button>
      <button
        onClick={changeAttr}
        style={{ display: 'none' }}
      >
        stop
      </button>
    </div>
  );
}

export default App;
