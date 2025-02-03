#include<vector>
#include<queue>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int n = maps.size();
    int m = maps[0].size();
    
    vector<vector<int>> d = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    vector<vector<int>> visited(n, vector<int>(m, 0));
    int answer = 1;
    int i = 0;
    int j = 0;
    queue<pair<int, int>> q;
    q.push({i, j});
    visited[i][j] = 1;
    
    while (!q.empty()) {
        int ra = q.size();
        for (int t = 0; t < ra; t++) {
            pair<int, int> f = q.front();
            
            int x = f.first;
            int y = f.second;
            q.pop();
            
            if (x == n-1 && y == m-1) return answer;
            
            for (const auto& dir:d) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m && not visited[nx][ny] && maps[nx][ny] == 1) {
                    visited[nx][ny] = 1;
                    q.push({nx, ny});
                }
            }
        }
        answer += 1;
    }
    
    return -1;
}