import React from 'react';
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../css/Header.css';


const Header = () => {

  const nav = useNavigate();


  return (
    <div className='header'>
      <button onClick={() => { nav('/'); }}>홈</button>
      <button onClick={() => { nav('/baseball'); }}>야구</button>
      <br />
      <br />
    </div>
  )
}

export default Header
