package practice;

class Test {
    public void display(int num1) {
        System.out.println(num1);
    }
    public void display(int num1, int num2) {
        System.out.println(num1 * num2);
    }
}


public class No017_Overloading {
    public static void main(String[] args) {
        Test t = new Test();
        t.display(1);
        t.display(1, 5);
    }
}
