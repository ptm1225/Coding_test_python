#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    stack<int> s;
    int length = progresses.size();
    int day = 0;
    int cnt;
    
    for (int i = length-1; i > -1; i--) {
        s.push((100-progresses[i] + speeds[i] - 1) / speeds[i]);
    }
    
    while (!s.empty()) {
        if (s.top() == day) {
            cnt = 0;
            while (!s.empty() and s.top() <= day) {
                s.pop();
                cnt++;
            }
            answer.push_back(cnt);
        }
        day++;
    }
    return answer;
}