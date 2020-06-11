import java.util.Scanner;
import java.lang.Integer;
import java.lang.Math;
import java.util.Random;

public class Mathematics {

    // Generic breaklines
    static void br(int foo) {
        String line = "=====";
        for (int i = 0; i < foo; i++) line += "=";
        System.out.println(line);
    }

    // Common retry function
    static void retry() { 
        System.out.println("Invalid answer. Please try again"); 
        br(65);
        main(null);
    }

    // Basic requirements function
    static String basereq(String x) {
        if (x.length() < 8 && x.matches("[0-9]+")) {}
        else retry();
        return x;
    }
    
    // Pythagoras Theorem
    static void pyth0(String x, String y, String z) {
        Scanner input = new Scanner(System.in);
        Random rng = new Random();
        br(65);
        System.out.println("What's " + x + " and " + y + "? (e.g. " + (rng.nextInt(10) + 1) + ", " + (rng.nextInt(10) + 1) + ")");
            String userInput = input.nextLine().toLowerCase();
            br(65);
            if (userInput.contains(", ")) {
                String[] inputA = userInput.split(", ");
                basereq(inputA[0]);
                basereq(inputA[1]);
                int b = Integer.parseInt(inputA[0]);
                int c = Integer.parseInt(inputA[1]);
                if (z.equals("a") || z.equals("b")) {
                    System.out.println(z + " = sqrt(" + c +"^2 - " + b + "^2)");
                    System.out.println(z + " = sqrt(" + c*c + " - " + b*b + ")");
                    System.out.println(z + " = sqrt(" + (c*c - b*b) + ")");
                    System.out.println(z + " = " + Math.sqrt(c * c - b * b));
                } else if (z.equals("c")) {
                    System.out.println(z + " = sqrt(" + b +"^2 + " + c + "^2)");
                    System.out.println(z + " = sqrt(" + b*b + " + " + c*c + ")");
                    System.out.println(z + " = sqrt(" + (b*b + c*c) + ")");
                    System.out.println(z + " = " + Math.sqrt(b * b + c * c));
                } else retry();
            } if (userInput.equals("back") || userInput.equals("prev")) pyth();
            else if (userInput.equals("exit") || userInput.equals("leave") || userInput.equals("quit")) System.exit(0);
            else retry();
            pyth0(x, y, z);
    }

    static void pyth() {
        Scanner input = new Scanner(System.in);
        System.out.println("Pythagoras Theorem: c^2 = a^2 + b^2\nWhat variable are you finding? (a, b, c)");
            String userInput = input.nextLine().toLowerCase();
            if (userInput.equals("a")) {
                System.out.println("a = sqrt(c^2 - b^2)");
                pyth0("b", "c", "a");
            } else if (userInput.equals("b")) {
                System.out.println("b = sqrt(c^2 - a^2)");
                pyth0("a", "c", "b");
            } else if (userInput.equals("c")) {
                System.out.println("c = sqrt(a^2 + b^2)");
                pyth0("a", "b", "c");
            } else if (userInput.equals("back") || userInput.equals("prev")) main(null);
            else if (userInput.equals("exit") || userInput.equals("leave") || userInput.equals("quit")) System.exit(0);
            else retry();
    }

    // Sine Rule

    public static void main(String[] args) {
        System.out.println("Welcome to the Mathinator v0.1 ALPHA! What mathematics fancy you?");
        System.out.println("1. Pythagoras Theorem   2. Sine Rule");
        Scanner input = new Scanner(System.in);
        String userInput = input.nextLine();
        br(65);

        if (userInput.equals("1")) pyth();
        else if (userInput.equals("2")) {}
        else if (userInput.equals("exit") || userInput.equals("leave") || userInput.equals("quit")) System.exit(0);
        else retry();
        
        main(null);
        input.close();
    }
}