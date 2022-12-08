import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class SecondPuzzle08 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day08\\08_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);
        
        char tmp;
        List<Integer> scenic_scores = new LinkedList<>();
        for (int i = 0; i < lines.size(); i++) {
            for (int j = 0; j < lines.get(i).length(); j++) {
                int sum_left = 0;
                int sum_right = 0;
                int sum_up = 0;
                int sum_down = 0;
                tmp = lines.get(i).charAt(j);

                for (int k = j - 1; k >= 0; k--) {
                    if (tmp <= lines.get(i).charAt(k)) {
                        sum_left++;
                        break;
                    } else {
                        sum_left++;
                    }
                }
                for (int k = j + 1; k < lines.get(i).length(); k++) {
                    if (tmp <= lines.get(i).charAt(k)) {
                        sum_right++;
                        break;
                    } else {
                        sum_right++;
                    }
                }
                for (int k = i - 1; k >= 0; k--) {
                    if (tmp <= lines.get(k).charAt(j)) {
                        sum_up++;
                        break;
                    } else {
                        sum_up++;
                    }
                }
                for (int k = i + 1; k < lines.size(); k++) {
                    if (tmp <= lines.get(k).charAt(j)) {
                        sum_down++;
                        break;
                    } else {
                        sum_down++;
                    }
                }

                scenic_scores.add(sum_left * sum_down * sum_right * sum_up);
            }
        }

        int max_scenic_score = Collections.max(scenic_scores);
        System.out.println("the max scenic score is " + max_scenic_score);
    }
}
