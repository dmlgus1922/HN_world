package practice;

class Car {
	private String modelName;
	private int modelYear;
	private String color;
	private int maxSpeed;
	private int currentSpeed;
	private int accelerationTime;
	
	Car(String modelName, int modelYear, String color, int maxSpeed) {
		this.modelName = modelName;
		this.modelYear = modelYear;
		this.color = color;
		this.maxSpeed = maxSpeed;
		this.currentSpeed = 0;
		this.accelerationTime = 0;
	}
	
	public String getModel() {
		return this.modelYear + "년식 " + this.color + " " + this.modelName;
	}
	
	public void accelerate(int speed, int second) {
		System.out.println(second + "초 동안 " + speed + "/s로 달림");
	}
	
	public String getMaxSpeed() {
		return "최대속도: " + this.maxSpeed;
	}
}

public class No014_Class {
	public static void main(String[] args) {
		Car mycar = new Car("K5", 2020, "흰색", 200);
		mycar.accelerate(100, 4);
		
		System.out.println(mycar.getModel());
		System.out.println(mycar.getMaxSpeed());
		
	}
}