import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FirstPuzzle02 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\_02\\FirstPuzzle02_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        // A - Rock, B - Paper, C - Scissors
        // X - Rock, Y - Paper, Z - Scissors
        int score = 0;
        for (String line : lines) {
            if (line.equals("A X")) score += 1 + 3;
            if (line.equals("A Y")) score += 2 + 6;
            if (line.equals("A Z")) score += 3 + 0;
            if (line.equals("B X")) score += 1 + 0;
            if (line.equals("B Y")) score += 2 + 3;
            if (line.equals("B Z")) score += 3 + 6;
            if (line.equals("C X")) score += 1 + 6;
            if (line.equals("C Y")) score += 2 + 0;
            if (line.equals("C Z")) score += 3 + 3;
        }
        System.out.println("My total score is " + score);
    }
}
