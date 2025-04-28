import React from 'react';
import { Link } from 'react-router-dom';
import '../css/Main.css';

const Home = () => {
    return (
        <div className="home">
            <h1>소개</h1>
            <p>안녕하세요! 저는 [이름]입니다.</p>
            <p>이메일: example@example.com</p>
            <p>전화번호: 010-1234-5678</p>
            <Link to="/game">
                <button>게임 페이지로 이동</button>
            </Link>
        </div>
    );
};

export default Home;