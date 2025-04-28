import React from 'react';
import { Link } from 'react-router-dom';
import '../css/Header.css';

const Header = () => {
    return (
        <header className="header">
            <nav>
                <ul>
                    <li><Link to="/">소개</Link></li>
                    <li><Link to="/career">경력</Link></li>
                    <li><Link to="/game">게임</Link></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
