import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FirstPuzzle07 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day07\\07_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        Map<String, Integer> values_map = new HashMap<>();
        String line = null;
        String temp_key = null;
        Integer temp_value = null;
        int sum = 0;
        for (int i = lines.size() - 1; i >= 0; i--) {
            line = lines.get(i);
            if (line.startsWith("$ cd")) {
                temp_key = line.substring(5);
                if (!temp_key.equals("..")) {
                    temp_value = 0;
                    int j = i + 1;
                    while (j < lines.size() && !lines.get(j).startsWith("$ cd")) {
                        if (lines.get(j).startsWith("dir")) {
                            temp_value += values_map.get(lines.get(j).substring(4));
                        } else if (!lines.get(j).startsWith("$ ls")) {
                            temp_value += Integer.parseInt(lines.get(j).substring(0, lines.get(j).indexOf(" ")));
                        }
                        j++;
                    }
                    values_map.put(temp_key, temp_value);
                    System.out.println(temp_key + " " + temp_value);
                    if (temp_value <= 100000)
                        sum += temp_value;
                }
            }
        }

        System.out.println(sum);
    }
}
