import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int n;
    static int [][] arr;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        int ans = 0;
        for (int i=0; i<n; i++) {
            String t = br.readLine();
            for(int j=0; j<n; j++) {
                switch (t.charAt(j)) {
                    case 'C': arr[i][j] = 1;
                        break;
                    case 'P': arr[i][j] = 2;
                        break;
                    case 'Z': arr[i][j] = 3;
                        break;
                    case 'Y': arr[i][j] = 4;
                        break;
                }
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                int t = fn(i,j);
                ans = Math.max(ans, t);
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n-1; j++) {
                int t1 = arr[i][j];
                int t2 = arr[i][j+1];
                arr[i][j] = t2;
                arr[i][j+1] = t1;
                int t = fn(i,j);
                ans = Math.max(ans, t);
                arr[i][j] = t1;
                arr[i][j+1] = t2;
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n-1; j++) {
                int t1 = arr[j][i];
                int t2 = arr[j+1][i];
                arr[j][i] = t2;
                arr[j+1][i] = t1;
                int t = fn(j,i);
                ans = Math.max(ans, t);
                arr[j][i] = t1;
                arr[j+1][i] = t2;
            }
        }
        System.out.println(ans);
    }
    public static int fn(int x, int y) {
        int ans = 0;
        int t = 0;

        for (int j=0; j<2; j++) {
            if (x == n-1 && j == 1) break;
            t = 0;
            for (int i=0; i<n-1; i++) {
                if (arr[x+j][i] == arr[x+j][i+1]) {
                    t++;
                } else {
                    ans = Math.max(ans, t+1);
                    t = 0;
                }
            }
            ans = Math.max(ans, t+1);
        }
        ans = Math.max(ans, t+1);
        t = 0;
        for (int j=0; j<2; j++) {
            if (y == n-1 && j == 1) break;
            t = 0;
            for (int i = 0; i < n - 1; i++) {
                if (arr[i][y+j] == arr[i + 1][y+j]) {
                    t++;
                } else {
                    ans = Math.max(ans, t + 1);
                    t = 0;
                }
            }
            ans = Math.max(ans, t+1);
        }
        return Math.max(ans, t+1);
    }
}
