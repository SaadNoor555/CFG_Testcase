#include<iostream>
using namespace std;


int main (int x, int y) {
   while (x!=y){
      if(x>y)
         x=x-y;
      else 
        y=y-x;
    }
   cout<< x;
}