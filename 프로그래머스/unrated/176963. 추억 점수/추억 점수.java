import java.util.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> map = new HashMap();
        for (int i=0; i<name.length; i++){
            map.put(name[i],yearning[i]);
        }
        for (int i=0; i<photo.length; i++){
            int tem = 0;
            for (String x: photo[i]){
                 tem += map.getOrDefault(x,0);
            }
            answer[i] = tem;
        }

        return answer;
    }
}