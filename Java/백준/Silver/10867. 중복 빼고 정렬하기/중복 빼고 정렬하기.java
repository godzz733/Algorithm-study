import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    static FastReader in = new FastReader();
    static FastWriter out = new FastWriter();

    // ======================== FastReader ========================
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

        // 공백으로 구분된 int 배열 읽기
        int[] readIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextInt();
            }
            return arr;
        }

        // 한 줄에 공백으로 구분된 int 배열 읽기
        int[] readIntArrayInLine() {
            String[] input = nextLine().split(" ");
            int[] arr = new int[input.length];
            for (int i = 0; i < input.length; i++) {
                arr[i] = Integer.parseInt(input[i]);
            }
            return arr;
        }

        // 공백으로 구분된 long 배열 읽기
        long[] readLongArray(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextLong();
            }
            return arr;
        }

        // String 배열 읽기 (한 줄씩)
        String[] readStringArray(int n) {
            String[] arr = new String[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextLine();
            }
            return arr;
        }

        // 한 줄에 공백으로 구분된 String 배열 읽기
        String[] readStringArrayInLine() {
            return nextLine().split(" ");
        }

        // 2차원 int 배열 읽기
        int[][] read2DIntArray(int n, int m) {
            int[][] arr = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = nextInt();
                }
            }
            return arr;
        }

        // 문자열을 char 배열로 읽기
        char[] readCharArray() {
            return nextLine().toCharArray();
        }

        // 2차원 char 배열 읽기 (그리드 형태)
        char[][] read2DCharArray(int n) {
            char[][] arr = new char[n][];
            for (int i = 0; i < n; i++) {
                arr[i] = readCharArray();
            }
            return arr;
        }
    }

    // ======================== FastWriter ========================
    static class FastWriter {
        private final BufferedWriter bw;

        public FastWriter() {
            this.bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        public void print(Object object) throws IOException {
            bw.append("").append(String.valueOf(object));
        }

        public void println(Object object) throws IOException {
            print(object);
            bw.append("\n");
        }

        public void printArray(int[] arr) throws IOException {
            for (int i = 0; i < arr.length; i++) {
                if (i != 0) bw.append(" ");
                bw.append(String.valueOf(arr[i]));
            }
            bw.append("\n");
        }

        public void printArray(long[] arr) throws IOException {
            for (int i = 0; i < arr.length; i++) {
                if (i != 0) bw.append(" ");
                bw.append(String.valueOf(arr[i]));
            }
            bw.append("\n");
        }

        public void print2DArray(int[][] arr) throws IOException {
            for (int[] row : arr) {
                printArray(row);
            }
        }

        public void close() throws IOException {
            bw.close();
        }

        public void flush() throws IOException {
            bw.flush();
        }
    }

    // ======================== 자주 사용하는 상수 ========================
    static final int INF = Integer.MAX_VALUE;
    static final long LINF = Long.MAX_VALUE;
    static final int MOD = 1000000007;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    // ======================== 메인 메소드 ========================
    public static void main(String[] args) throws IOException {
        solve();
        out.flush();
        out.close();
    }

    // ======================== 구현부 ========================
    static void solve() throws IOException {
        // 여기에 문제 풀이 구현

        // 예시 1: 정수 하나 읽기
        // int n = in.nextInt();

        // 예시 2: 정수 배열 읽기 (n개)
        // int n = in.nextInt();
        // int[] arr = in.readIntArray(n);

        // 예시 3: 한 줄에 있는 정수들 읽기
        // int[] arr = in.readIntArrayInLine();

        // 예시 4: 문자열 읽기
        // String s = in.nextLine();

        // 예시 5: 2차원 배열 읽기
        // int n = in.nextInt();
        // int m = in.nextInt();
        // int[][] grid = in.read2DIntArray(n, m);

        // 예시 6: 출력
        // out.println(answer);
        // out.printArray(answerArray);
        int n = in.nextInt();
        int [] arr = new int[2002];
        for (int i: in.readIntArray(n)) {
            arr[i+1000] = i+2000;
        }
        Arrays.stream(arr).filter(i -> i != 0)
                .forEach(i -> System.out.print(i-2000 + " "));

    }

}