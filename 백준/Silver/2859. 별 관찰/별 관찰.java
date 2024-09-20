import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int a = fn(br.readLine());
        int c = fn(br.readLine());
        int b = fn(br.readLine());
        int d = fn(br.readLine());
        ArrayList<Integer> arr= new ArrayList<>();
        Map<Integer, String> map = new HashMap<>();
        map.put(0,"Saturday");
        map.put(1,"Sunday");
        map.put(2,"Monday");
        map.put(3,"Tuesday");
        map.put(4,"Wednesday");
        map.put(5,"Thursday");
        map.put(6,"Friday");
        for (int i=0; i<=1440; i++) {
            arr.add(a + b*i);
        }
        for (int i=0; i<=1440; i++) {
            int t = c+d*i;
            if (arr.contains(t)) {
                System.out.println(map.get(((t) / 1440)%7));
                System.out.println(String.format("%02d:%02d",(t%1440)/60,((t%1440)%60)));
                System.exit(0);
            }
        }
        System.out.println("Never");
    }
    public static int fn(String t) {
        int a = Integer.parseInt(t.substring(0,2));
        int b = Integer.parseInt(t.substring(3,5));
        return a*60 + b;
    }
}
