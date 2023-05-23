package practice;

public class No018_Recursive {
    static int recur(int n) {
        if (n == 1) {
            return 1;
        }
        return n + recur(n - 1);
    }
    public static void main(String[] args){
        int result = recur(4);
        System.out.println(result);
    }
}

