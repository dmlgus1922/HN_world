import React from 'react';
import '../css/Main.css';

const Main = () => {
  const name = 'react';
  return (
    <div className='main'>
      {name === 'react' && <p>hi</p>}
      <div id='intro'>
          여기에다가 내 소개 넣을거셈
      </div>
      <div id='info'>
        
      </div>
      <div id='skills'>
        여기에는 내 스킬들 넣을거
      </div>

    </div>
  )
}

export default Main;
