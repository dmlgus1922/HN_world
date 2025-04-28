package practice;

class Math {
    int a = 10; // 인스턴스 변수
    int b = 20; // 인스턴스 변수

    int add() { // 인스턴스 메소드
        return a + b;
    }
    
    static int add(int x, int y) { // 클래스 메소드
        return x + y;
    }
}

public class No020_Method {
    public static void main(String[] args) {
        Math calc = new Math();
        System.out.println(Math.add(10, 30));
        System.out.println(calc.add());
        System.out.println(calc.add(20,100));
    }
    
}
