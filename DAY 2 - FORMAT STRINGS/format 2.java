public class Test {
    public void vulnerableMethod(String user_input) {
        System.out.printf(user_input); // Vulnerable: directly using user input
    }
}
