#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer(right-left+1);
    
    for (int idx = 0; idx <= right-left; idx++) {
        answer[idx] = (max((idx+left)/n, (idx+left)%n)+1);
    }
    
    return answer;
}