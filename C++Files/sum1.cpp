#include<iostream>

using namespace std;
//comment
int main() {
    int x = 10;
    int y=6;
    int sum = x+y;
    while(x>y) {
        sum+=x;
        x--;
        y++;
    }
    cout<< x<< endl;
}