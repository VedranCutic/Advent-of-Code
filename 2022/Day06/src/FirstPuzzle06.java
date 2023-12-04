import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FirstPuzzle06 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day06\\06_input.txt";
        Path path = Path.of(fileName);
        String line = Files.readString(path, StandardCharsets.UTF_8);

        char first;
        char second;
        char third;
        char fourth;
        int index = 0;
        for (int i = 0; i < line.length(); i++) {
            first = line.charAt(i);
            second = line.charAt(i + 1);
            third = line.charAt(i + 2);
            fourth = line.charAt(i + 3);
            if (first != second && first != third && first != fourth && second != third && second != fourth && third != fourth) {
                index = i + 4;
                break;
            }
        }
        System.out.println(index + " characters has been processed");

    }
}
