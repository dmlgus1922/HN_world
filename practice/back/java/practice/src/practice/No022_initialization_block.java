package practice;

class Car1 {
	private String modelName;
	private int modelYear;
	private String color;
	private int maxSpeed;
	private int currentSpeed;
	
	{ //인스턴스 초기화 블럭
		this.currentSpeed = 0;
	}
	
	Car1(){} //생성자 1
	// 생성자 2
	Car1(String modelName, int modelYear, String color, int maxSpeed){ 
		this.modelName = modelName;
		this.modelYear = modelYear;
		this.color = color;
		this.maxSpeed = maxSpeed;
	}
	
	public int getSpeed() {
		return currentSpeed;
	}
	
	public void changeSpeed(int speed) {
		this.currentSpeed = speed;
	}
}


public class No022_initialization_block {
	public static void main(String[] args) {
		Car1 myCar = new Car1();
		System.out.println(myCar.getSpeed());
		Car1 myCar2 = new Car1("sonata", 2023, "red", 200);
		myCar2.changeSpeed(10);
		System.out.println(myCar2.getSpeed());
		
				
	}
}
