// 스킬트리
class Solution {
    public int solution(String skill, String[] skill_trees) {
        // 가능한 스킬트리 개수를 리턴하라
        int answer = 0;
        
        for(int i = 0; i < skill_trees.length; i++) {
            String temp = "";
            for(int j = 0; j < skill_trees[i].length(); j++) {
                String c = Character.toString(skill_trees[i].charAt(j));
                if(skill.contains(c)) {
                    temp += c;
                }
            }
            if (skill.startsWith(temp)) answer++;
        }
        
        return answer;
    }
}