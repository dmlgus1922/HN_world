import React from 'react';
import '../css/Main.css';

const Career = () => {
    return (
        <div className="career">
            <h1>경력</h1>
            <ul>
                <li>
                    <h2>회사 A</h2>
                    <p>직책: 소프트웨어 엔지니어</p>
                    <p>기간: 2020년 1월 - 2023년 12월</p>
                    <p>주요 업무: 웹 애플리케이션 개발</p>
                </li>
                <li>
                    <h2>회사 B</h2>
                    <p>직책: 프론트엔드 개발자</p>
                    <p>기간: 2018년 3월 - 2019년 12월</p>
                    <p>주요 업무: UI/UX 디자인 및 구현</p>
                </li>
            </ul>
        </div>
    );
};

export default Career;