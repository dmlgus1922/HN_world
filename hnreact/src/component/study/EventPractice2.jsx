import { useState } from 'react';

const EventPractice2 = () => {
    const [form, setForm] = useState({
        userName: '',
        message:''
    });

    const handleClick = () => {
        alert(form.userName + ': ' + form.message);
        setForm({
            userName:'',
            message:''
        });
    }

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleClick();
        }
    }

    return (
        <div>
            <input
                type="text"
                placeholder="유저 이름"
                name="userName"
                value={form.userName}
                onChange={e => { setForm({...form, userName: e.target.value}); }}
            />
            <input
                type="text"
                placeholder="아무말"
                name="message"
                value={form.message}
                onChange={e => { setForm({...form, message: e.target.value}); }}
                onKeyPress={handleKeyPress}
            />
            <button onClick={handleClick}>
                확인
            </button>
        </div>

    )
}

export default EventPractice2;