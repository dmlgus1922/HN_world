package practice;

class Car3 {
    private String modelName;
    private int modelYear;
    private String color;
    private int maxSpeed;
    private int currentSpeed;

    Car3(String modelName, int modelYear, String color, int maxSpeed) {
        this.modelName = modelName;
        this.modelYear = modelYear;
        this.color = color;
        this.maxSpeed = maxSpeed;
        this.currentSpeed = 0;
    }

    Car3() {
        // this 메소드로 다른 생성자 부르기
        // 메소드 시그니처가 같은 생성자를 부름
        this("소나타", 2023, "검정색", 200);
    }

    public String getModel() {
        return this.modelYear + "년식 " + this.color  + " " + this.modelName;
    }
}

public class No016_This {
    public static void main(String[] args) {
        Car3 myCar = new Car3();
        System.out.println(myCar.getModel());
    }
}
