package practice;

public class No010_Array_prac2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] grade1 = {70, 80, 90};
		int[] grade2 = new int[] {70, 80, 90};
		int[] grade3;
		// grade3 = {70, 80, 90}; error. 선언만 된 배열은 이 방법으로 초기화 불가능
		grade3 = new int[] {70, 80, 90};
		
		for (int i: grade3) {
			System.out.print(i + " ");
		}
		
	}

}
