import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FirstPuzzle10 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day10\\10_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        int register = 1;
        int cycles = 0;
        int signal_strengh_sum = 0; // the cycle number multiplied by the value of the X register

        String instruction;
        int addition;
        for (String line : lines) {
            instruction = line.substring(0, 4);
            if (instruction.equals("noop")) {
                cycles++;
                if ((cycles - 20) % 40 == 0) {
                    System.out.println("cylcle " + cycles + " register " + register);
                    signal_strengh_sum += cycles * register;
                }
            } else {
                if (line.charAt(5) == '-') {
                    addition = Integer.parseInt(line.substring(6));
                    cycles += 2;
                    if ((cycles - 20) % 40 == 0) {
                        System.out.println("cylcle " + cycles + " register " + register);
                        signal_strengh_sum += cycles * register;
                    }
                    register -= addition;
                } else {
                    addition = Integer.parseInt(line.substring(5));
                    cycles += 2;
                    if ((cycles - 20) % 40 == 0) {
                        System.out.println("cylcle " + cycles + " register " + register);
                        signal_strengh_sum += cycles * register;
                    }
                    register += addition;
                }
            }
        }
        System.out.println("The sum is " + signal_strengh_sum);
    }
}
