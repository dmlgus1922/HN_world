package practice;

public class No021_recursiveSum {
	static int recursiveSum(int n) {
		if (n==1) {
			return 1;
		}
		return n + recursiveSum(n-1);
	}
	public static void main(String[] args) {
		System.out.println(recursiveSum(4));
	}
}
