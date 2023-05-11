package practice;

public class No004_Type {

	public static void main(String[] args) {
		// byte형 → short형 → int형 → long형 → float형 → double형
		//           char형 ↗
		
		// int에서 double로 타입 변환. double > int 범위이므로 데이터 손실이 없으니 변환 가능
		double num1 = 10;
		
		// int num2 = 3.14; double형 데이터를 int로 초기화하면 데이터 손실이 생기므로 error 발생
		
		// 연산을 위해 float 데이터가 double로 자동변환됨. (범위: double > float)
		double num3 = 7.0f + 3.14;
		
		System.out.println(num1);
		System.out.println(num3);
		
		
		// (type cast)
		int num4 = 1, num5 = 4;
		double result1 = num4 / num5;
		double result2 = (double) num4 / num5;
		
		// int끼리의 연산으로 result1은 정수인 0으로 초기화
		System.out.println(result1);
		// type cast를 적용한 result2는 double로 초기화됨
		System.out.println(result2);
		
	}

}
