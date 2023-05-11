package practice;

public class No007_DoWhile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i = 1;
		do {
			System.out.println("do/while 반복문이 "+i+"번째 실행 중");
			i++;
		} while (i < 5);
		
		System.out.println("do/while 반복문 종료 후: " + i);
	}

}
