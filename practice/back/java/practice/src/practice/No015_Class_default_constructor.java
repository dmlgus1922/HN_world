package practice;

class Car2 {
	private String modelName = "아반떼";
	private String color = "흰색";
	private int modelYear = 2023;
	
	public void getModel() {
		System.out.println(this.modelYear + "년식 " + this.color + " " + this.modelName);
	}
	
}

public class No015_Class_default_constructor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Car2 mycar = new Car2();
		mycar.getModel();
	}

}
