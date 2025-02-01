#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    long long n = num;
    int answer = 0;
    while (n != 1){
        if (n % 2 == 0){
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        answer++;
        if (answer >= 500) {
            return -1;
        }
    }
    return answer;
}