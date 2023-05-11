package practice;

public class No003_Number {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// byte 데이터 -128 ~ 127
		byte num1 = 127;
		byte num2 = -128;
		
		num1++;
		num2--;
		
		// 오버플로우, 언더플로우(범위 벗어남) 계산한 값이 나오지 않음.
		System.out.println(num1);
		System.out.print(num2);
		
		float num3 = (float) 3.14;
		double num4 = 3.141592;
		
	}

}
