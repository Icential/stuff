import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    String name;
    String race;
    String prof;
    String[] races = {"Asura", "Sylvari", "Human", "Norn", "Charr"};
    String[] professions = {"Warrior", "Guardian", "Revenant", "Ranger", "Thief", "Engineer", "Necromancer", "Mesmer", "Elementalist"};

    public Main(String charName, String charRace, String charProf) {
        if (charName.endsWith(" ")) charName = charName.replaceAll(" +$", "");
        charName = nameCap(charName);
        charRace = firstCap(noSpace(charRace));
        charProf = firstCap(noSpace(charProf));

        if (charName.length() >= 17) {
            System.out.println(charName + " exceeds the character limit!");
        } else name = charName;

        if (Arrays.stream(races).anyMatch(charRace::equals)) {
            race = charRace;
        } else System.out.println(charRace + " is not a valid race!");

        if (Arrays.stream(professions).anyMatch(charProf::equals)) {
            prof = charProf;
            if (prof.equals(professions[0])) {
                Scanner userInput = new Scanner(System.in);
                System.out.println("What elite specialization? (Berserker, Spellbreaker, Core)");
                String eliteSpec = userInput.nextLine();
                userInput.close();
                switch (firstCap(noSpace(eliteSpec))) {
                    case "Berserker":
                        prof = eliteSpec;
                        break;
                    case "Spellbreaker":
                        prof = eliteSpec;
                        break;
                    case "Core":
                        prof = "Warrior";
                        break;
                    default:
                        System.out.println("That's not a Warrior elite specialization!");
                        prof = "Warrior";
                        break;
                }
            }
        } else System.out.println(charProf + " is not a valid profession!");
    }

    public void id() {
        br();
        if (this.name != null) System.out.println("Name: " + this.name);
        if (this.race != null) System.out.println("Race: " + this.race);
        if (this.prof != null) System.out.println("Profession: " + this.prof);
        br();
    }

    static void greetings() {
        System.out.println("Greetings user!");
        br();
    }

    static String[] arrayify(String foo) {
        String[] array = foo.split(", ");
        return array;
    }

    static void br() {
        System.out.println("=====================");
    }

    static String noSpace(String foo) {
        if (foo.contains(" ")) foo.replaceAll(" ", "");
        return foo;
    }

    static void hasSpace(String foo) {
        if (foo.contains(" ")) System.out.println(foo + " has space!");
    }

    static String firstCap(String foo) {
        return foo.substring(0, 1).toUpperCase() + foo.substring(1);
    }

    static String nameCap(String foo) {
        char[] chars = foo.toLowerCase().toCharArray();
        boolean found = false;
        for (int i = 0; i < chars.length; i++) {
            if (!found && Character.isLetter(chars[i])) {
                chars[i] = Character.toUpperCase(chars[i]);
                found = true;
            } else if (Character.isWhitespace(chars[i]) || chars[i]=='.' || chars[i]=='\'') found = false;
        }
        return String.valueOf(chars);
    }

    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        System.out.println("Please put your character identifications (Name, Race, Core Profession):");
        String charID = userInput.nextLine();
        userInput.close();
        String[] idSplit = arrayify(charID);
        Main newChar = new Main(idSplit[0], idSplit[1], idSplit[2]);
        newChar.id();
    }
}