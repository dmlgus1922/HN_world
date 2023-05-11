package practice;

public class No006_ForWhileLabel {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		outerloop:
			for (int i = 2; i <= 9; i++) {
				innerloop:
				for (int j = 2; j <=9; j++) {					
					if (i == 5) {
						break outerloop;
					}
					if (i == 3) {
						continue innerloop;
					}
					System.out.println(i + "*" + j + "=" + i*j);
				}
			}
	}

}
