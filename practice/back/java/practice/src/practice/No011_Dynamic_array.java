package practice;

public class No011_Dynamic_array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] arr = new int[2][];
		arr[0] = new int[2];
		arr[1] = new int[3];
		
		int k = 1;
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = k;
				System.out.print(arr[i][j] + " ");
				k++;
			}
			System.out.println();
		}
		
		System.out.println();
		
		int[][] arr2 = {
				{1,2,3,4},
				{5,6},
				{7,8,9}
		};
		
		for (int[] a: arr2) {
			for (int num: a) {
				System.out.print(num + " ");
			}
			System.out.println();
		}

	}

}
