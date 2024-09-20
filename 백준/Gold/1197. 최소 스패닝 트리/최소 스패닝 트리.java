import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int [] p;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int ans = 0;
        ArrayList<int []> arr = new ArrayList<>();
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            arr.add(new int [] {a-1,b-1,c});
        }
        Collections.sort(arr,new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });

        p = new int[n];
        for (int i=0; i<n; i++){p[i] = i;}
        for (int i=0; i<m; i++) {
            int [] tem = arr.get(i);
            int a = find_parent(tem[0]);
            int b = find_parent(tem[1]);
            if (a != b) {
                union(tem[0],tem[1]);
                ans += tem[2];
            }
        }
        System.out.println(ans);
    }
    static int find_parent(int x){
        if (x != p[x]) return find_parent(p[x]);
        return p[x];
    }
    static void union(int a, int b){
        a = find_parent(a);
        b = find_parent(b);
        if (a<b) p[a] = b;
        else p[b] = a;
    }
}
