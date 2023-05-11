package practice;

public class No009_Array_prac {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr1 = new int[3]; // 길이 3의 int형 배열
		arr1[0] = 10;
		arr1[1] = 20;
		arr1[2] = 30;
		
		int[] arr2 = new int[3];
		arr2[0] = 10; // 초기화되지 않은 원소는 데이터형식에 따라 자동으로 초기화됨. (int는 0)
		
		for (int i = 0; i < arr1.length; i++) {
			System.out.print(arr1[i] + " ");
		}
		
		System.out.println();
		
		for (int i = 0; i < arr2.length; i++) {
			System.out.print(arr2[i] + " ");
		}
		
	}

}
