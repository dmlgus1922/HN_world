import { React, useState, useRef } from 'react';
import '../css/Main.css';

const NumberBaseball = () => {
  // 정답 여부
  const [answer, setAnswer] = useState(false);
  // 만들어낸 숫자
  const [answerNum, setAnswerNum] = useState('');
  // 만들어낸 숫자 {각 자릿수 : 인덱스}
  const [answerNumIdx, setAnswerNumIdx] = useState({});

  // 입력하는 숫자
  const [userInput, setUserInput] = useState('');
  // 인풋 ref
  const inputRef = useRef();
  // 적었던 숫자
  const [history, setHistory] = useState([]);

  // 숫자 생성 함수
  const mkNum = () => {
    if (answerNum === '') {
      let num = '';
      while (num.length < 4) {
        const randNum = Math.floor(Math.random() * 10);
        num = num.includes(randNum) ? num : num + randNum;
      }
      setAnswerNum(num);

      let numIdx = {};
      for (let i = 0; i < 4; i++) {
        numIdx[num[i]] = i
      }
      setAnswerNumIdx(numIdx);
      alert('🤖 삐빅. 숫자를_생각했습니다.');
    } else {
      alert('숫자는 이미 생성되었답니다. 😎');
    }
  }

  const checkNumber = () => {
    if (!answerNum) {
      alert('숫자 만들기 버튼부터 눌러주세요!');
      return
    }
    const inputNumber = parseInt(userInput);
    if (userInput.length !== 4 || userInput != inputNumber) {
      alert('숫자 네 자리로 입력해주세요 🤣');
      inputRef.current.value = '';
      return
    } else if (history.includes(userInput)) {
      alert('이미 확인하신 번호네요 😅\n다른 숫자를 찾아볼까요?');
      inputRef.current.value = '';
      return
    }

    for (let n of userInput) {
      if (userInput.indexOf(n) !== userInput.lastIndexOf(n)) {
        alert('각각 다른 숫자 네 개를 입력하세요 😊');
        inputRef.current.value = '';
        return
      }
    }

    if (userInput === answerNum) {
      inputRef.current.value = '';
      let correct = [];
      for (let i = 0; i < 100; i++) {
        correct = correct.concat(['그는 신이야.. 어떻게 맞춘거지.. 그는 신이야.. 어떻게 맞춘거지.. 그는 신이야.. 어떻게 맞춘거지..']);
      }
      setAnswer(true);
      setHistory(correct);
      setTimeout(() => {
        let again = '';
        for (let i = 0; i < 100; i++) {
          again += '다시해!!!';
        }
        alert(again);
      }, 500);
      return
    }

    let st = 0;
    let ball = 0;
    for (let i = 0; i < 4; i++) {
      const idx = answerNumIdx[userInput[i]]
      if (idx !== undefined) {
        if (idx === i) {
          st++;
        } else {
          ball++;
        }
      }
    }
    if (!st && !ball) {
      setHistory(history.concat(userInput + ` : 아웃! (${st} 스트라이크 ${ball} 볼)`));
    } else {
      setHistory(history.concat(userInput + ` : ${st} 스트라이크 ${ball} 볼!`));
    }
    inputRef.current.value = '';
  }

  const playAgain = () => {
    alert('😁 제가 잠깐 흥분을 했네요. 숫자 만들기 버튼을 다시 눌러주세요~❤')
    setAnswerNum('');
    setHistory([]);
    setAnswer(false);
  }

  return (
    <div className='main'>
      나는야 숫자야구왕! 
      <br />
      <br />
      <button onClick={mkNum}>숫자 만들기~</button>
      <br />
      <br />
      <input type="text" ref={inputRef} onChange={(e) => { setUserInput(e.target.value); }}
        placeholder="숫자 네 자리" />
      <button onClick={checkNumber}>이거 맞니?!</button>
      {
        answer
          ?
          <div>
            <h1>👹👹👹👹👹👹👹👹👹👹👹👹👹👹</h1>
            <h1>!!!!!!당장 다시 해!!!!!!</h1>
            <h1>👹👹👹👹👹👹👹👹👹👹👹👹👹👹</h1>

            <button onClick={playAgain}>죽고싶지 않으면 다시 하기</button>
          </div>
          :
          <></>
      }
      <div>
        {
          answer
            ?
            history.map((data, idx) => {
              return <h3 key={idx}>{data}</h3>
            })
            :
            history.map((data, idx) => {
              return <p key={idx}>{data}</p>
            })
        }
      </div>


    </div>
  )
}

export default NumberBaseball;
