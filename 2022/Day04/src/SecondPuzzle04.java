import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class SecondPuzzle04 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day04\\04_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        int commaIndex;
        String firstElf;
        String secondElf;
        int firstElf_lower;
        int firstElf_upper;
        int secondElf_lower;
        int secondElf_upper;
        int sum = 0;

        for (String line : lines) {
            commaIndex = line.lastIndexOf(',');
            firstElf = line.substring(0, commaIndex);
            secondElf = line.substring(commaIndex + 1);

            firstElf_lower = Integer.parseInt(firstElf.substring(0, firstElf.lastIndexOf('-')));
            firstElf_upper = Integer.parseInt(firstElf.substring(firstElf.lastIndexOf('-') + 1));
            secondElf_lower = Integer.parseInt(secondElf.substring(0, secondElf.lastIndexOf('-')));
            secondElf_upper = Integer.parseInt(secondElf.substring(secondElf.lastIndexOf('-') + 1));

            if ((firstElf_lower <= secondElf_upper && firstElf_lower >= secondElf_lower)
                    || (firstElf_upper <= secondElf_upper && firstElf_upper >= secondElf_lower)
                    || (secondElf_lower <= firstElf_upper && secondElf_lower >= firstElf_lower)
                    || (secondElf_upper <= firstElf_upper && secondElf_upper >= firstElf_lower)) {
                sum++;
            }
        }
        System.out.println("The sum is " + sum);
    }
}
