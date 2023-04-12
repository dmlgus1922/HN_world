import { Routes, Route } from 'react-router-dom';

import Home from './component/Home';
import Header from './component/Header';
import NumberBaseball from './component/NumberBaseball';
import Footer from './component/Footer';

import './css/App.css';

function App() {
  return (
    <div className="App">
      <Header></Header>
      <Routes>
        <Route path='/' element={<Home/>}></Route>
        <Route path='/baseball' element={<NumberBaseball />}></Route>
      </Routes>
      <Footer></Footer>
    </div>
  );
}

export default App;
