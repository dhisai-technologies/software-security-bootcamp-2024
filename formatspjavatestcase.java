import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; 
        } catch (Exception e) {  
            System.out.println("An error occurred");
        }
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();  
        System.out.println("Your age is: " + age);
    }
}
