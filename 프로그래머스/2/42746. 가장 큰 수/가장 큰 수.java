import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        ArrayList<String> arr= new ArrayList();
        for (int i=0; i<numbers.length; i++){
            arr.add(Integer.toString(numbers[i]));
        }
        Collections.sort(arr, new Comparator<String>() {
             @Override
             public int compare(String s1, String s2) {
                return s1.concat(s2).compareTo(s2.concat(s1));
             }
        });
        for (int i=numbers.length-1; i>=0; i--){
            answer += arr.get(i);
        }
        if (answer.charAt(0) == '0') return "0";
        return answer;
    }
}