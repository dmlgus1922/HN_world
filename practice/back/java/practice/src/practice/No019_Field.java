package practice;

class Field {
    static int classVar = 10; // 클래스 변수
    int instanceVar = 20; // 인스턴스 변수
}


public class No019_Field {
    public static void main(String[] args){
        int var = 30; // 지역변수
        System.out.println("지역변수 참조");
        System.out.println("지역변수: " + var + "\n"); 
        
        // 인스턴스 생성
        Field myField1 = new Field(); //인스턴스 생성
        Field myField2 = new Field();

        //클래스 변수 참조
        System.out.println("클래스 변수 참조");
        System.out.println("클래스에서 참조: " + Field.classVar);
        System.out.println("인스턴스에서 참조: " + myField1.classVar);
        System.out.println("인스턴스에서 참조: " + myField2.classVar + "\n");

        myField1.classVar = 100; // 인스턴스에서 클래스 변수 값 변경
        System.out.println("인스턴스에서 클래스 변수 변경");
        System.out.println("클래스에서 참조: " + Field.classVar);
        System.out.println("인스턴스에서 참조: " + myField1.classVar);
        System.out.println("인스턴스에서 참조: " + myField2.classVar + "\n");

        System.out.println("인스턴스 변수 참조");
        System.out.println(myField1.instanceVar);
        System.out.println(myField2.instanceVar + "\n" );

        System.out.println("인스턴스 변수 값 변경");
        myField1.instanceVar = 100;
        System.out.println("인스턴스 변수 참조");
        System.out.println(myField1.instanceVar);
        System.out.println(myField2.instanceVar + "\n" );

    }
}
