package practice;
import java.util.*;
import java.util.stream.*;

public class Prac1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String[] arr = new String[] {"넷", "둘", "셋", "하나"};
		
		Stream<String> stream1 = Arrays.stream(arr);
		stream1.forEach(e -> System.out.print(e + " "));
		System.out.println();
		
		Stream<String> stream2 = Arrays.stream(arr, 1, 3);
		stream2.forEach(e -> System.out.print(e + " "));
	}

}
