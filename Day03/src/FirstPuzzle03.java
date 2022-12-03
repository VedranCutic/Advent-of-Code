import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FirstPuzzle03 {
    public static void main(String[] args) throws IOException {
        Path path = Path.of("C:\\AOC\\Day03\\03_input.txt");
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        String firstCompartment;
        String secondCompartment;
        int size;
        int priorities_sum = 0;
        int indexOfSame = 0;
        for (String line : lines) {
            size = line.length();
            firstCompartment = line.substring(0, size / 2);
            secondCompartment = line.substring(size / 2, size);
            for (int i = 0; i < size / 2; i++) {
                for (int j = 0; j < size / 2; j++) {
                    if (firstCompartment.charAt(i) == secondCompartment.charAt((j))) {
                        indexOfSame = i;
                        break;
                    }
                }
            }
            char same = firstCompartment.charAt(indexOfSame);
            int addition = Character.isUpperCase(same) ? 26 : 0;
            same = Character.toUpperCase(same);
            priorities_sum += addition + (same - 64);
        }
        System.out.println("Sum of priorities " + priorities_sum);
    }
}
