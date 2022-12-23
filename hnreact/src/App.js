import Header from './component/Header';
import Main from './component/Main';
import Footer from './component/Footer';
import { Routes, Route } from 'react-router-dom';

import './css/App.css';

function App() {
  return (
    <div className="App">
      <Header></Header>
      <Main></Main>
      <Footer></Footer>
    </div>
  );
}

export default App;
