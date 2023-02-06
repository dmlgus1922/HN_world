import React from 'react'

const Login = () => {
    return (
        <div style={{textAlign:'center'}}>
            <div>

                Welcom to KakaoTalk
            </div>
            <div>

                if you have a Kakao Account,
                log in with your email or phone number.
            </div>
            <input type="text" placeholder='Email or phone number'/>
            <br />
            <input type="password" placeholder='Password' />
            <br />
            <button>
                Log In
            </button>
            <br />
            <button>
                Sign up
            </button>
            <br />
            <p>Find Kakao Account or Password</p>
        </div>
    )
}

export default Login;