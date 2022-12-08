import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FirstPuzzle08 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day08\\08_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        int sum = 0;
        char tmp;
        for (int i = 0; i < lines.size(); i++) {
            for (int j = 0; j < lines.get(i).length(); j++) {
                tmp = lines.get(i).charAt(j);
                if (i == 0 || i == lines.size() - 1 || j == 0 || j == lines.get(i).length() - 1) {
                    sum++;
                } else {
                    boolean visible_left = true;
                    boolean visible_right = true;
                    boolean visible_up = true;
                    boolean visible_down = true;
                    for (int k = j - 1; k >= 0; k--) {
                        if (tmp <= lines.get(i).charAt(k)) {
                            visible_left = false;
                            break;
                        }
                    }
                    for (int k = j + 1; k < lines.get(i).length(); k++) {
                        if (tmp <= lines.get(i).charAt(k)) {
                            visible_right = false;
                            break;
                        }
                    }
                    for (int k = i - 1; k >= 0; k--) {
                        if (tmp <= lines.get(k).charAt(j)) {
                            visible_up = false;
                            break;
                        }
                    }
                    for (int k = i + 1; k < lines.size(); k++) {
                        if (tmp <= lines.get(k).charAt(j)) {
                            visible_down = false;
                            break;
                        }
                    }
                    if (visible_down || visible_left || visible_right || visible_up) sum++;
                }
            }
        }

        System.out.println("the sum is " + sum);
    }
}
