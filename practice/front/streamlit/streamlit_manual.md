## 간단한 streamlit 사용법

### 1. 위젯

	① 웹 화면을 구성하는 데 필요한 태그를 streamlit 제공 위젯으로 간단히 생성할 수 있다.

	② 보통 streamlit을 import할 때 alias를 st로 사용하며 st.write()의 형태로 위젯을 생성한다.

	③ 위젯의 상태값이 변경되면 기본적으로 코드 전체를 재실행한다.
	
	④ 자주 사용했던 위젯
		- write: p 태그 생성. 입력한 문자열을 브라우저에 나타낸다.
		- button: button 태그 생성. 상태값으로 boolean을 가지며 default는 False, 클릭 시 True로 변경된다.
		- text_input: input 태그를 생성. 문자열을 입력받을 수 있다.
		- image: 이미지 array를 argument로 받아 브라우저에 이미지를 표출한다.
		- container
			· 위젯을 생성할 수 있는 영역을 선언할 때 사용한다.
			· 파이썬은 코드를 위에서 아래로 차례로 읽는다. 특정 상호작용이 일어날 때 상태값을 변경하고 싶은 위젯이 상호작용이 일어나는 곳보다 위에 있을 때, container를 이용해 미리 변수에 선언한 후 해당 변수를 이용해 위젯을 다룬다.

### 2. 세션

	① 1-③에 의해 변수에 값을 저장하고 상호작용을 통해 이를 변경해도 변경 사항이 업데이트되지 않는다. 이를 해결하기 위해 세션 기능이 도입되었다.

	② 세션은 st.session_state에 저장되며 딕셔너리 형태, attribute형태로 접근할 수 있다. (st.session_state[test_session] 혹은 st.session_state.test_session)
	
	③ 세션을 사용하기 전 미리 저장해야 한다.

### 3. 캐싱
	① 1-③에 의해 용량이 큰 데이터, 함수 등이 매번 재실행될 때마다 load되는 것을 방지하기 위해 캐싱 기능이 존재한다.
	
	② 데코레이터를 이용해 함수 위에 @st.cache와 같은 형태로 사용한다.

### 4. 콜백
	① input, button 등 상태값이 변하는 위젯에 콜백 함수를 넣을 수 있다.
	
	② text_input은 on_cahnge, button은 on_click의 파라미터를 가지고 미리 생성한 함수를 아규먼트로 넣어준다.


