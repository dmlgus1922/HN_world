package practice;

public class No008_Class_prac {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		class A {}
		class B extends A {}	
		A a = new A();
		
		B b = new B();
		
		System.out.println(a instanceof A);
		System.out.println(a instanceof B);
		System.out.println(b instanceof A);
		System.out.println(b instanceof B);
		
		
	}

}
