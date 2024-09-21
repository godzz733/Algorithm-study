import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int n, m, k;
    static long[] tree;
    static long[] arr;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int size = (int) Math.ceil(Math.log(n) / Math.log(2));
        tree = new long[2 << (size + 1)];
        arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        m += k;
        init(); // 비재귀 초기화
        while (m-- > 0) {
            String[] line = br.readLine().split(" ");
            int what = Integer.parseInt(line[0]);
            if (what == 1) {
                int index = Integer.parseInt(line[1]);
                long val = Long.parseLong(line[2]);
                update(index - 1, val); // 비재귀 업데이트
            } else {
                int left = Integer.parseInt(line[1]);
                int right = Integer.parseInt(line[2]);
                sb.append(query(left - 1, right - 1)).append("\n"); // 비재귀 쿼리
            }
        }
        System.out.println(sb);
    }

    // 비재귀 세그먼트 트리 초기화
    static void init() {
        // 리프 노드에 값 넣기
        for (int i = 0; i < n; i++) {
            tree[n + i] = arr[i];
        }

        // 내부 노드 초기화
        for (int i = n - 1; i > 0; i--) {
            tree[i] = tree[i << 1] + tree[i << 1 | 1];
        }
    }

    // 비재귀 쿼리
    static long query(int l, int r) {
        l += n;
        r += n;
        long sum = 0;
        while (l <= r) {
            if ((l & 1) == 1) sum += tree[l++]; // 왼쪽 자식
            if ((r & 1) == 0) sum += tree[r--]; // 오른쪽 자식
            l >>= 1;
            r >>= 1;
        }
        return sum;
    }

    // 비재귀 업데이트
    static void update(int idx, long val) {
        idx += n;
        tree[idx] = val;
        while (idx > 1) {
            idx >>= 1;
            tree[idx] = tree[idx << 1] + tree[idx << 1 | 1];
        }
    }
}
