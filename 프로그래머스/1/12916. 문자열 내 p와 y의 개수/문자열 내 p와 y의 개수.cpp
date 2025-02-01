#include <string>
#include <iostream>
#include <cctype>
using namespace std;

bool solution(string s)
{
    int a = 0;
    int b = 0;
    for (char c: s){
        if (tolower(c) == 'p'){
            a = a+1;
        } else if (tolower(c) == 'y'){
            b = b+1;
        }
    }
    if (a == b){
        return true;
    } else{
        return false;
    }
}