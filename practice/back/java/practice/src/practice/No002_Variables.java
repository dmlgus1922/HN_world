package practice;

public class No002_Variables {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num;
		num = 10; // 선언만 한 변수는 사용 불가능. 초기화를 해야 사용할 수 있다.
		System.out.println(num);
		
		int num1, num2; // 같은 타입의 두 변수 한 번에 선언
		double num3 = 3.14; // 선언과 동시에 초기화
		double num4 = 3.13, num5 = 3.12; // 같은 타입의 두 변수를 한 번에 선언하며 초기화
		// num1 = 1.1; // type mismatch로 error 발생
		
		
		final int AGE = 28; // 상수는 반드시 선언과 동시에 초기화하여야 함
		
		// 문자형 데이터. 작은 정수나 문자 하나를 담을 수 있음
		char alpha = 'a';
		System.out.println(alpha);
		
		boolean t = true;
		System.out.println(t);
		
		// 실수 연산의 오차
		double num6 = 0.1;
		for (int i = 0; i < 1000; i++) {
			num6 += 0.1;
		}
		System.out.println(num6);
		
		// float은 소수점 6째 자릿수까지 정확히 표현, 그 이상은 정확하지 않음
		// double은 15자리까지
		float num7 = 1.23456789f;
		double num8 = 1.23456789;
		System.out.println(num7);
		System.out.println(num8);
	}

}
