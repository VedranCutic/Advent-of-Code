import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class SecondPuzzle01 {
    public static void main(String[] args) throws IOException {
        String filename = "C:/AOC/_01/FirstPuzzle01_input.txt";
        Path path = Path.of(filename);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        int tmp = 0;
        int first = 0;
        int second = 0;
        int third = 0;
        for (String line : lines) {
            if (!line.isBlank()) {
                tmp += Integer.parseInt(line);
            } else {
                if (tmp > first) {
                    second = first;
                    first = tmp;
                } else if (tmp > second) {
                    third = second;
                    second = tmp;
                } else if (tmp > third) third = tmp;
                tmp = 0;
            }
        }
        int sum = first + second + third;
        System.out.println("first " + first);
        System.out.println("second " + second);
        System.out.println("third " + third);
        System.out.println("The sum of the first three is " + sum);
    }
}
