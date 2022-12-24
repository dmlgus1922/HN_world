import React from 'react';
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../css/Header.css';


const Header = () => {



  return (
    <div className='header'>
      <div>
        
        <a href="#intro">소개</a>
        <a href="#info">정보</a>
        <a href="#skills">기술</a>
      </div>
      이것은 헤더
    </div>
  )
}

export default Header
