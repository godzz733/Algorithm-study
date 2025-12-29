import java.math.BigInteger;
import java.util.*;
import java.io.*;

public class Main {
    static FastReader in = new FastReader();
    static FastWriter out = new FastWriter();
    private static final int [] dx = {1,-1,0,0};
    private static final int [] dy = {0,0,1,-1};
    public static void main(String[] args) throws IOException {
        solve();
        out.flush();
        out.close();
    }
    static void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<Object> tokens = new ArrayList<>();
        for (int i = 0; i < (n<<1)-1; i++) {
            String input = br.readLine().trim();
            // 연산자인지 숫자인지 판별하여 리스트에 저장
            if (input.equals("+") || input.equals("-") || input.equals("*") || input.equals("/")) {
                tokens.add(input);
            } else {
                tokens.add(new BigInteger(input));
            }
        }

        // 1단계: 곱셈(*)과 나눗셈(/) 먼저 처리
        List<Object> afterMD = new ArrayList<>();
        for (int i = 0; i < tokens.size(); i++) {
            Object token = tokens.get(i);

            if (token.equals("*") || token.equals("/")) {
                BigInteger left = (BigInteger) afterMD.remove(afterMD.size() - 1);
                BigInteger right = (BigInteger) tokens.get(++i);

                if (token.equals("*")) {
                    afterMD.add(left.multiply(right));
                } else {
                    afterMD.add(floorDivide(left, right));
                }
            } else {
                afterMD.add(token);
            }
        }

        // 2단계: 덧셈(+)과 뺄셈(-) 처리
        BigInteger result = (BigInteger) afterMD.get(0);
        for (int i = 1; i < afterMD.size(); i += 2) {
            String op = (String) afterMD.get(i);
            BigInteger nextVal = (BigInteger) afterMD.get(i + 1);

            if (op.equals("+")) {
                result = result.add(nextVal);
            } else {
                result = result.subtract(nextVal);
            }
        }

        System.out.println(result.toString());

    }
    // 소수점 내림(Floor Division) 구현
    public static BigInteger floorDivide(BigInteger dividend, BigInteger divisor) {
        // BigInteger의 기본 divide는 0을 향해 버림(Truncate) 처리됨
        BigInteger[] res = dividend.divideAndRemainder(divisor);
        BigInteger quotient = res[0];
        BigInteger remainder = res[1];

        // 나머지가 존재하고, 두 수의 부호가 다르면 결과값에서 1을 더 빼줌 (내림)
        if (remainder.signum() != 0 && (dividend.signum() != divisor.signum())) {
            quotient = quotient.subtract(BigInteger.ONE);
        }
        return quotient;
    }
    // ======================== 최강 속도 FastReader (Byte Level) ========================
    static class FastReader {
        private static final int BUFFER_SIZE = 1 << 16;
        private final DataInputStream din;
        private final byte[] buffer;
        private int bufferPointer, bytesRead;

        public FastReader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String next() throws IOException {
            StringBuilder sb = new StringBuilder();
            byte c = read();
            while (c <= ' ') c = read();
            while (c > ' ') {
                sb.append((char) c);
                c = read();
            }
            return sb.toString();
        }

        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return neg ? -ret : ret;
        }

        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return neg ? -ret : ret;
        }

        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9')
                    ret += (c - '0') / (div *= 10);
            }
            return neg ? -ret : ret;
        }

        public String nextLine() throws IOException {
            StringBuilder sb = new StringBuilder();
            byte c = read();
            while (c == '\n' || c == '\r') c = read();
            while (c != '\n' && c != '\r' && c != -1) {
                sb.append((char) c);
                c = read();
            }
            return sb.toString();
        }

        // --- 편의 메서드들 ---
        public int[] readIntArray(int n) throws IOException {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = nextInt();
            return arr;
        }

        public long[] readLongArray(int n) throws IOException {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = nextLong();
            return arr;
        }

        public int[][] read2DIntArray(int n, int m) throws IOException {
            int[][] arr = new int[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++) arr[i][j] = nextInt();
            return arr;
        }

        public char[] readCharArray() throws IOException {
            return next().toCharArray();
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1) buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead) fillBuffer();
            return buffer[bufferPointer++];
        }
    }

    // ======================== 최적화된 FastWriter ========================
    static class FastWriter {
        private final BufferedWriter bw;

        public FastWriter() {
            this.bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        public void print(Object o) throws IOException { bw.write(String.valueOf(o)); }
        public void println(Object o) throws IOException { bw.write(String.valueOf(o)); bw.write("\n"); }

        // Primitive 최적화 (Boxing 방지)
        public void print(int i) throws IOException { bw.write(Integer.toString(i)); }
        public void println(int i) throws IOException { bw.write(Integer.toString(i)); bw.write("\n"); }

        public void printArray(int[] arr) throws IOException {
            for (int i = 0; i < arr.length; i++) {
                print(arr[i]);
                if (i != arr.length - 1) bw.write(" ");
            }
            bw.write("\n");
        }

        public void flush() throws IOException { bw.flush(); }
        public void close() throws IOException { bw.close(); }
    }
}