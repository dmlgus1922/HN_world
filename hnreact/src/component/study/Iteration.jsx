import { useState } from 'react';

const Iteration = () => {
    const [names, setNames] = useState([
        { id: 1, text: '눈사람' },
        { id: 2, text: '얼음' },
        { id: 3, text: '눈' },
        { id: 4, text: '바람' },
    ]);
    const [inputText, setInputText] = useState('');
    const [nextId, setNextId] = useState(5);

    const onChange = e => setInputText(e.target.value);
    const onRemove = (id) => {
        setNames(names.filter(data => {
            return data.id !== id
        }))
    }
    const insert = () => {
        setNames(names.concat([{id: nextId, text: inputText}]));
        setNextId(nextId + 1);
        setInputText('');            
    }


    const nameList = names.map((value, idx) => {
        return <li key={value.id} onDoubleClick={() => {onRemove(value.id)}}>{value.text}</li>
    })

    return (
        <div>
            <input type="text" value={inputText} onChange={onChange} />
            <button onClick={insert}>추가</button>
            <ul>{nameList}</ul>

        </div>
    );
}

export default Iteration;