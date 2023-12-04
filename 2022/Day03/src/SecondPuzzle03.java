import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class SecondPuzzle03 {

    public static int sharedLetterPriority(String first, String second, String third) {
        int sharedLetterPriority = 0;

        boolean[] firstB = new boolean[52];
        boolean[] secondB = new boolean[52];
        boolean[] thirdB = new boolean[52];

        //we set the boolean to true for every priority of a certain line
        for (int i = 0; i < first.length(); i++) {
            char character = first.charAt(i);
            int addition = Character.isUpperCase(character) ? 26 : 0;
            character = Character.toUpperCase(character);
            int index = addition + (character - 64);
            firstB[index - 1] = true;
        }
        for (int i = 0; i < second.length(); i++) {
            char character = second.charAt(i);
            int addition = Character.isUpperCase(character) ? 26 : 0;
            character = Character.toUpperCase(character);
            int index = addition + (character - 64);
            secondB[index - 1] = true;
        }
        for (int i = 0; i < third.length(); i++) {
            char character = third.charAt(i);
            int addition = Character.isUpperCase(character) ? 26 : 0;
            character = Character.toUpperCase(character);
            int index = addition + (character - 64);
            thirdB[index - 1] = true;
        }

        //now we calculate shared priorities(letters)
        for (int i = 0; i < 52; i++) {
            if (firstB[i]) {
                if (secondB[i]) {
                    if (thirdB[i]) {
                        sharedLetterPriority = i + 1;
                        break;
                    }
                }
            }
        }

        return sharedLetterPriority;
    }

    public static void main(String[] args) throws IOException {
        Path path = Path.of("C:\\AOC\\Day03\\03_input.txt");
        List<String> lines = Files.readAllLines(path);

        String firstLine;
        String secondLine;
        String thirdLine;
        int priorities_sum = 0;
        for (int i = 0; i < lines.size(); i++) {
            firstLine = lines.get(i++);
            secondLine = lines.get(i++);
            thirdLine = lines.get(i);
            int addition = sharedLetterPriority(firstLine, secondLine, thirdLine);
            priorities_sum += addition;
        }
        System.out.println("The sum of priorities is " + priorities_sum);
    }
}
