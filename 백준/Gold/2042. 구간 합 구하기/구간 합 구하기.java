import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int n,m,k;
    static long [] tree;
    static long [] arr;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int size = (int)Math.ceil(Math.log(n) / Math.log(2));
        tree = new long[2 << (size + 1)];
        arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }
        m += k;
        init(1,0,n-1);
        while (m-- > 0) {
            String [] line = br.readLine().split(" ");
            int what = Integer.parseInt(line[0]);
            if (what == 1) {
                int index = Integer.parseInt(line[1]);
                long val = Long.parseLong(line[2]);
                update(1, 0, n-1, index-1, val);
            } else {
                int left = Integer.parseInt(line[1]);
                int right = Integer.parseInt(line[2]);
                sb.append(query( 1, 0, n-1, left-1, right-1)).append("\n");
            }
        }
        System.out.println(sb);
    }
    static void init(int node, int st, int end) {
        if (st == end) {
            tree[node] = arr[st];
        }
        else {
            init(node<<1, st, (st+end) /2 );
            init(node*2+1,(st+end)/2 + 1, end);
            tree[node] = tree[node<<1] + tree[node*2 + 1];
        }
    }
    static long query(int node, int st, int end, int l, int r) {
        if (l > end || r < st) return 0;
        if (l <= st && r >= end) return tree[node];
        long lsum = query(node<<1, st, (st+end) >> 1, l, r);
        long rsum= query(node*2 + 1, (st+end)/2 + 1, end, l, r);
        return lsum + rsum;
    }
    static void update(int node, int st, int end, int idx, long val) {
        if (idx < st || idx > end) return;
        if (st == end) {
            tree[node] = val;
            arr[idx] = val;
            return;
        }
        update(node<<1, st, (st+end) >> 1, idx, val);
        update(node*2 + 1, ((st+end) >> 1)+1, end, idx, val);
        tree[node] = tree[node<<1] + tree[node*2 + 1];
    }
}
