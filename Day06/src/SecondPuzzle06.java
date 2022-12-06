import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class SecondPuzzle06 {

    public static boolean checkDuplicity(String substring) {
        char[] array_subs = substring.toCharArray();
        for (int i = 0; i < substring.length(); i++) {
            for (int j = i + 1; j < substring.length(); j++) {
                if (array_subs[i] == array_subs[j]) return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day06\\06_input.txt";
        Path path = Path.of(fileName);
        String line = Files.readString(path, StandardCharsets.UTF_8);

        String message_marker = null;
        char[] mm_array = new char[14];
        int tmp;
        int index = 0;
        for (int i = 0; i < line.length() - 13; i++) {
            message_marker = line.substring(i, i + 14);
            boolean check = checkDuplicity(message_marker);
            if (!check) {
                index = i + 14;
                break;
            }
        }
        System.out.println(index + " characters has been processed");

    }
}
