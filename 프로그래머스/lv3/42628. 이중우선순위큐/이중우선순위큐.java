import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        		TreeMap<Integer,Integer> map = new TreeMap<>();
		int[] answer = {0,0};
		for (String t: operations) {
			String [] input = t.split(" ");
			String a = input[0];
			Integer b = Integer.parseInt(input[1]);
			if (a.equals("I")) map.put(b, map.getOrDefault(b, 0)+1);
			else {
				if (map.isEmpty()) continue;
				if (b == -1) {
					if (map.get(map.firstKey()) == 1) map.pollFirstEntry();
					else map.put(map.firstKey(),map.get(map.firstKey())-1);
				} else {
					if (map.get(map.lastKey()) == 1) map.pollLastEntry();
					else map.put(map.lastKey(),map.get(map.lastKey())-1);
				}
			}
		}
		if (map.isEmpty()){
			answer[0] = answer[1] = 0;
		} else {
			answer[1] = map.firstKey();
			answer[0] = map.lastKey();
		}
        return answer;
    }
}