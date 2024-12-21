public class Test {
    public String vulnerableMethod(String user_input) {
        return String.format(user_input); // Vulnerable: directly using user input
    }
}
