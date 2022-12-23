import React from 'react';
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../css/Header.css';


const Header = () => {

  const nav = useNavigate();

  const movePart = (e) => {
    console.log(e.target.value)

  }

  const temp = [];
  for (let i = 0; i < 100; i++) {
    temp.push(<br></br>)
  }

  return (
    <div className='header'>
      <div>
        {/* <button className='nav' onClick={movePart} value='intro'>
          소개
        </button>
        <button className='nav' onClick={movePart} value='info'>
          정보
        </button>
        <button className='nav' onClick={movePart} value='skills'>
          스킬
  </button> */}
        <a href="#intro">소개</a>
        <a href="#info">정보</a>
        <a href="#skills">기술</a>
      </div>
      이것은 헤더
      {temp}
    </div>
  )
}

export default Header
