import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class FirstPuzzle01 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:/AOC/_01/FirstPuzzle01_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        String tmp_line;
        int tmp_value = 0;
        int max = 0;
        for (String line : lines) {
            tmp_line = line;
            if (!tmp_line.isBlank()) {
                tmp_value += Integer.parseInt(tmp_line);
            } else {
                if (tmp_value > max) max = tmp_value;
                System.out.println(max);
                tmp_value = 0;
            }
        }
        System.out.println("Max is " + max);
    }
}
