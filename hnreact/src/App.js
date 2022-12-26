import { Component } from 'react';
import { Routes, Route } from 'react-router-dom';

import Header from './component/Header';
import Main from './component/Main';
import Footer from './component/Footer';

import Test from './component/study/Test';
import Counter from './component/study/Counter';
import Say from './component/study/Say';
import EventPractice from './component/study/EventPractice';
import EventPractice2 from './component/study/EventPractice2';
import ValidationSample from './component/study/ValidationSample';
import ScrollBox from './component/study/ScrollBox';
import Iteration from './component/study/Iteration';

import './css/App.css';

// function App() {
//   return (
//     <div className="App">
//       {/* <Header></Header>
//       <Main></Main>
//       <Footer></Footer> */}
//       <ValidationSample></ValidationSample>
//       <EventPractice2></EventPractice2>
//       <EventPractice></EventPractice>
//       <Say></Say>
//       <Counter></Counter>
//       <Test name={'이름'} favoriteNumber={1}>
//         리액트
//         <div>
//           djdasd
//         </div>
//       </Test>
//     </div>
//   );
// }

class App extends Component {
  render() {
    return (
      <div>
        {/* <ValidationSample></ValidationSample> */}
        <Iteration></Iteration>
        {/* <ScrollBox ref={(ref) => this.scrollBox = ref}></ScrollBox>
        <button onClick={() => {this.scrollBox.scrollToBottom()}}>맨밑으로 이동</button> */}
      </div>
    );
  }
}

export default App;
