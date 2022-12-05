import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class FirstPuzzle05 {

    public static void parseStacks(List<String> lines, List<Stack<String>> stacks, int numOfStacks) {
        for (int i = 0; i < numOfStacks; i++) {
            Stack<String> tmpStack = new Stack<>();
            stacks.add(tmpStack);
        }
        for (int i = 0; i < numOfStacks; i++) {
            for (String line : lines) {
                if (line.indexOf("[") == 0) {
                    if (line.charAt(4 * i + 1) != ' ')
                        stacks.get(i).push(String.valueOf(line.charAt(4 * i + 1)));
                }
            }
        }
        for (int i = 0; i < numOfStacks; i++) {
            Stack<String> tmp = new Stack<>();
            int size = stacks.get(i).size();
            for (int j = 0; j < size; j++)
                tmp.push(stacks.get(i).pop());
            stacks.get(i).addAll(tmp);
        }
    }

    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day05\\05_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);
        List<Stack<String>> stacks = new LinkedList<>();

        int numOfStacks = 0;
        for (String line : lines) {
            if (!(line.indexOf("[") == 0)) {
                numOfStacks = Integer.parseInt(String.valueOf(line.charAt(line.length() - 1)));
                break;
            }
        }

        // we parse input to get all the stacks
        parseStacks(lines, stacks, numOfStacks);

        for (String line : lines) {
            int moved = -1;
            int from = -1;
            int to = -1;
            if ((line.indexOf("m") == 0)) {
                for (int i = 0; i < line.length(); i++) {
                    int f_index = line.indexOf('f');
                    String moved_s = line.substring(5, f_index - 1);
                    moved = Integer.parseInt(moved_s);

                    String from_s = line.substring(f_index + 5, f_index + 6);
                    from = Integer.parseInt(from_s);

                    to = Integer.parseInt(String.valueOf(line.charAt(line.length() - 1)));
                }
                for (int i = 0; i < moved; i++) {
                    if (!stacks.get(from - 1).empty())
                        stacks.get(to - 1).push(stacks.get(from - 1).pop());
                }
            }
        }

        System.out.println("at the top of every stack is >> ");
        for (int i = 0; i < numOfStacks; i++) {
            System.out.print(stacks.get(i).pop());
        }

    }
}
