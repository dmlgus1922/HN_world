package practice;

public class No012_Array_2D {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] arr = new int[2][3]; // 원소가 0으로 저장됨. (int라서)
		
		for (int[] i: arr) {
			for (int j: i) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
		System.out.println();
		
		int k = 1;
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = k;
				k += 10;
			}
		}
		
		for (int[] i: arr) {
			for (int j: i) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
		System.out.println();
		
		
		String[][] arr2 = new String[2][2];
		for (String[] i: arr2) {
			for (String j: i) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
		System.out.println();
		
		String s = "a";
		
		for (int i = 0; i < arr2.length; i++) {
			for (int j = 0; j < arr2[i].length; j ++) {
				arr2[i][j] = s;
				s += 'a';
			}
		}
		
		for (String[] i: arr2) {
			for (String j: i) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
		System.out.println();
		
		int[][] arr3 = {
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9}
		};
		for (int[] i: arr3) {
			for (int j: i) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
		
	}

}
