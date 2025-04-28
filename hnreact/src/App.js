import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Header from './component/Header';
import Footer from './component/Footer';
import Home from './component/Home';
import Career from './component/Career';
import NumberBaseball from './component/NumberBaseball';
import './css/App.css';

function App() {
    return (
        <div className="App">
            <Header />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/career" element={<Career />} />
                <Route path="/game" element={<NumberBaseball />} />
            </Routes>
            <Footer />
        </div>
    );
}

export default App;
