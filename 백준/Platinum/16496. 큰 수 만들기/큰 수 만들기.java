import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        String answer = "";
        ArrayList<String> arr= new ArrayList();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++){
            arr.add(st.nextToken());
        }
        Collections.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.concat(s2).compareTo(s2.concat(s1));
            }
        });
        for (int i=n-1; i>=0; i--){
            answer += arr.get(i);
        }
        if (answer.charAt(0) == '0') {
            System.out.println("0");
        } else {
            System.out.println(answer);
        }
    }
}
