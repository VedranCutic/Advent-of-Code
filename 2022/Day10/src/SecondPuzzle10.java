import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class SecondPuzzle10 {
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\AOC\\Day10\\10_input.txt";
        Path path = Path.of(fileName);
        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);

        int register = 1;
        int cycles = 0;

        String[][] CRT = new String[6][40];
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 40; j++) {
                CRT[i][j] = ".";
            }
        }

        String instruction;
        int addition;
        for (String line : lines) {
            instruction = line.substring(0, 4);
            if (instruction.equals("noop")) {
                if (cycles % 40 == register || cycles % 40 == register - 1 || cycles % 40 == register + 1) {
                    CRT[cycles / 40][cycles % 40] = "#";
                }
                cycles++;
            } else {
                if (line.charAt(5) == '-') {
                    addition = Integer.parseInt(line.substring(6));
                    if (cycles % 40 == register || cycles % 40 == register - 1 || cycles % 40 == register + 1) {
                        CRT[cycles / 40][cycles % 40] = "#";
                        CRT[cycles / 40][cycles % 40] = "#";
                    }
                    cycles++;
                    if (cycles % 40 == register || cycles % 40 == register - 1 || cycles % 40 == register + 1) {
                        CRT[cycles / 40][cycles % 40] = "#";
                        CRT[cycles / 40][cycles % 40] = "#";
                    }
                    cycles++;
                    register -= addition;
                } else {
                    addition = Integer.parseInt(line.substring(5));
                    if (cycles % 40 == register || cycles % 40 == register - 1 || cycles % 40 == register + 1) {
                        CRT[cycles / 40][cycles % 40] = "#";
                        CRT[cycles / 40][cycles % 40] = "#";
                    }
                    cycles++;
                    if (cycles % 40 == register || cycles % 40 == register - 1 || cycles % 40 == register + 1) {
                        CRT[cycles / 40][cycles % 40] = "#";
                        CRT[cycles / 40][cycles % 40] = "#";
                    }
                    cycles++;
                    register += addition;
                }
            }
        }


        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 40; j++) {
                System.out.print(CRT[i][j]);
            }
            System.out.println();
        }

    }
}
