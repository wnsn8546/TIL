import java.util.*;
// boj 1260 DFS, BFS
// 주어진 그래프를 DFS, BFS로 탐색한 결과를 출력하는 프로그램을 작성하기
// 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
// 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
// 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
// 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
// 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

public class Main {

    static int[][] graph;
    static boolean[] visited;
    static Queue<Integer> q = new LinkedList<>();
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 정점 개수
        int M = sc.nextInt(); // 간선 개수
        int V = sc.nextInt(); // 시작 정점 번호

        graph = new int[N+1][N+1]; // 편의상 0번을 사용하지 않고, N+1 크기로 만든다.
        visited = new boolean[N+1];

        for(int i = 0;i < M;i++) { // 연결된 간선의 정보의 시작, 끝을 입력 받아 배열에 표시한다.
            int start = sc.nextInt();
            int end = sc.nextInt();

            graph[start][end] = 1;
            graph[end][start] = 1;
        }

        dfs(V); // dfs 호출
        System.out.println();
        visited = new boolean[N+1]; // bfs 호출 전에 초기화
        bfs(V); // bfs 호출
    }
    public static void dfs(int V) {
        visited[V] = true;
        System.out.print(V + " ");

        for(int i = 1; i < graph[V].length;i++) {
            if(visited[i] == false && graph[V][i] == 1) {
                dfs(i);
            }
        }
    }

    public static void bfs(int V) {
        q.offer(V);
        visited[V] = true;

        while (!q.isEmpty()) {
            V = q.poll();
            System.out.print(V + " ");
            for(int i = 1; i < graph[V].length;i++) {
                if(visited[i] == false && graph[V][i] == 1) {
                    visited[i] = true;
                    q.offer(i);
                }
            }
        }
    }
}