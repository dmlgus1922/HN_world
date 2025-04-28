package practice;

import java.util.Arrays;

public class No013_Copy_Array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr1 = new int[] {1,2,3,4,5};
		int newlen = 10;
		
		int[] arr2 = new int[newlen];
//		System.arraycopy(arr1, 0, arr2, 0, arr1.length);
		// 1. System 클래스의 arraycop() 메소드
		// params - 1: 복사할 소스 array, 2: 소스 array에서 복사를 시작할 인덱스
		// 3: 복사한 원소를 넣을 array, 4: 소스 array 시작 인덱스에서부터 복사할 원소의 개수(소스 array 범위를 벗어나면 error)
		System.arraycopy(arr1, 1, arr2, 2, 2);
		for (int num: arr2) {
			System.out.print(num + " ");
		}
		System.out.println();
		
		// 2. Arrays 클래스의 copyOf() 메소드
		// 복사할 array의 첨부터 복사함. 범위를 벗어나면 명시한 자료형의 기본 데이터로 저장
		int[] arr3 = Arrays.copyOf(arr1, 10);
		for (int num: arr3) {
			System.out.print(num + " ");
		}
		System.out.println();
		
		// Object 클래스의 clone() 메소드
		int[] arr4 = (int[])arr1.clone();
		for (int num: arr4) {
			System.out.print(num + " ");
		}
		System.out.println();
		
		
		
	}

}
