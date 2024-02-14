import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        // 두 팀으로 나누어서 상대팀 진영을 파괴하는 게임이다.
        // 따라서 각 팀은 상태 진영에 최대한 빨리 도착해야한다.
        // 검은 부분은 벽이며, 흰색을 갈 수 있는 길이다.
        // 캐릭터는 동, 서, 남, 북 으로 한 칸 씩 이동하며, 맵을 벗어나지는 못한다.
        // 상대진영에 도착하기위해서 필요한 최소 칸 수 구하기.
        // 도달 하지 못한다면 -1을 리턴.
        // 0은 벽, 1은 길.
        // 캐릭터의 시작점은 맨 좌측상단의(1,1), 상대 진영은 맨 우측하단의(n,m)
        // bfs로 최단거리를 구한다.
        // 탐색하면서 카운트를 한다.
        int answer = 0;

        int n = maps.length; // 세로길이 n
        int m = maps[0].length; // 가로길이 m
        Queue<int[]> q = new LinkedList<>(); // bfs 에 사용할 큐
        int[][] visited = new int[n][m]; // 방문처리 기록할 visited

        int dx[] = {-1, 1, 0, 0}; // 4방향 탐색을 위한 dx
        int dy[] = {0, 0, -1, 1}; // dy

        q.offer(new int[]{0, 0}); // 시작점을 넣고 한 칸 표시를 한다.
        visited[0][0] = 1; // 방문처리 한다.

        while (!q.isEmpty()) { // 큐가 빌때까지 반복한다.
            int temp[] = q.poll(); // 큐에서 첫번째 값을 꺼내면서 임시 변수에 넣어준다,
            int x = temp[0]; // x, y값을 바꿔주고
            int y = temp[1];


            if (x == n-1 && y == m-1) {
                //answer = count; // (n,m) 상대진영에 도착했다면 answer에 값을 넣어주고,
                answer = visited[x][y];
                break; // while문을 끝낸다.
            }

            for (int i = 0; i < 4; i++) { // 4방향 탐색을 하면서,
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 벽이 아니고, 맵 바깥의 범위가 아닐때, 아직 방문하지 않았고 길이라면, +1을 하여 큐에 넣고 방문처리를한다.

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if(maps[nx][ny] == 0) continue;
                if(visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    q.offer(new int[]{nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        if (answer == 0) {
            answer = -1;
        }
        return answer;
    }
}